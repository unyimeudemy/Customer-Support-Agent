from celery import shared_task
from google import genai
from decouple import config
from main.lib.intent_classifier import classify_intent
from main.lib import kb_collection_store
from main.lib.workflow_map import WORKFLOW_MAP
from main.lib.workflow_executor  import WorkflowExecutor
from main.lib import global_variables 
import re
import json
import time




def build_prompt_1(**kwargs):
    CUSTOMER_MESSAGE = kwargs.get('CUSTOMER_MESSAGE', '')
    WORKFLOW_DESCRIPTION = kwargs.get('WORKFLOW_DESCRIPTION', '')
    PREVIOUS_QUESTION_BY_LLM = kwargs.get('PREVIOUS_QUESTION_BY_LLM', '')
    SLOT_ENTITY_LAST_STATE = kwargs.get('SLOT_ENTITY_LAST_STATE', '')

    return f"""
    You are a customer service agent.

    You will receive:
    - CUSTOMER_MESSAGE: "{CUSTOMER_MESSAGE}"
    - WORKFLOW_DESCRIPTION: "{WORKFLOW_DESCRIPTION}"
    - PREVIOUS_QUESTION_BY_LLM: "{PREVIOUS_QUESTION_BY_LLM}"
    - CURRENT_JSON: {SLOT_ENTITY_LAST_STATE}

    --- Expected behavior ---

    1. If CUSTOMER_MESSAGE is unrelated to PREVIOUS_QUESTION_BY_LLM:
        Return: "{CUSTOMER_MESSAGE}" (as plain string, no extra words).

    2. If CUSTOMER_MESSAGE answers PREVIOUS_QUESTION_BY_LLM:
        Update CURRENT_JSON accordingly.
        
    3. If CUSTOMER_MESSAGE is a single word or short phrase that fits any field of CURRENT_JSON:
        Update CURRENT_JSON accordingly.

    --- IMPORTANT OUTPUT FORMAT ---

    - Always return **only** the updated JSON.
    - Use this format: {{"field_1": "value_1", "field_2": "value_2"}}
    - Do NOT include ```json or ``` or any extra explanation or text.

    --- Example ---

    Input: "John Doe"
    Output: {{"name": "John Doe", "age": ""}}

    """


def build_prompt_2(**kwargs):
    CUSTOMER_MESSAGE = kwargs.get('CUSTOMER_MESSAGE', '')
    WORKFLOW_DESCRIPTION = kwargs.get('WORKFLOW_DESCRIPTION', '')
    SLOT_ENTITY_LAST_STATE = kwargs.get('SLOT_ENTITY_LAST_STATE', '')

    return f"""
    You are a customer service AI agent.

    The customer said: "{CUSTOMER_MESSAGE}".
    The current process is: "{WORKFLOW_DESCRIPTION}".

    The system requires filling all the keys in this target JSON object:
    {SLOT_ENTITY_LAST_STATE}

    Instruction:
    - Look at the keys that have empty values ("").
    - Randomly select only one key that still has an empty value.
    - Politely ask the customer for the value of that key.
    - The question should follow this exact format:

      "Kindly provide your [key_name]."

    Example outputs:
      - Kindly provide your email.
      - Kindly provide your date_of_purchase.
      - Kindly provide your phone.

    Do not explain anything else. Only return the question following the format above.
    Do not add any greeting, closing or extra text.
    """


def build_prompt_3(**kwargs):
    WORKFLOW_DESCRIPTION = kwargs.get('WORKFLOW_DESCRIPTION', '')
    SLOT_ENTITY_LAST_STATE = kwargs.get('SLOT_ENTITY_LAST_STATE', '')

    return f"""
    You are a customer service AI agent.

    The customer has requested to start the process: "{WORKFLOW_DESCRIPTION}".
    However, no information has been provided yet.

    The system requires the following fields from this JSON object:
    {SLOT_ENTITY_LAST_STATE}

    Instruction:
    - Select the first key from the JSON object.
    - Ask the customer to provide the value for that key.
    - The question should follow this exact format:

      "Kindly provide your [key_name]."

    Example:
      - Kindly provide your email.
      - Kindly provide your date_of_purchase.

    Do not explain anything. Do not generate any other text. Only return the question.
    """


def generate_answer_for_enquiry_questions(query, context):
    """Generate response summary"""
    prompt = f"""
    You are a customer service AI agent called Allena for Piraxx limited. 
    Only provide answers based on the information explicitly found in the context below. 
    Do not make assumptions. If unsure, say "I don't know."

    ### Question:
    {query}

    ### Context:
    {context}

    ### Answer:
    """

    client = genai.Client(api_key=config('GEMINI_API_KEY'))
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=prompt
    )
    return response.text


def generate_answer_for_workflow(prompt):

    client = genai.Client(api_key=config('GEMINI_API_KEY'))
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=prompt
    )
    return response.text


def send_message_over_telegram(response, recipient_id):
    from main.lib.telegram_client import telegram_client_wrapper_instance

    try:
        if telegram_client_wrapper_instance:
            telegram_client_wrapper_instance.queue_message(
                recipient=recipient_id,
                message=response
            )
    except Exception as e:
        print(f"chat io chat process failed with exceptions: {e}")


def has_empty_field(data):
    return any(value == "" for value in data.values())


def parse_llm_response(response: str) -> dict:
    """
    Clean LLM response and parse it into a Python dict.
    Handles cases where LLM wraps response in ```json ... ``` code blocks.
    """
    # Remove code block markers if present
    clean_response = re.sub(r"```json|```", "", response).strip()
    
    try:
        data = json.loads(clean_response)
        return data
    except json.JSONDecodeError as e:
        print("Failed to parse JSON:", e)
        return response


@shared_task(
    bind=True,
    queue="io_tasks",
    autoretry_for=(),  
    retry_backoff=False,
    max_retries=0,
    acks_late=False
)
def handle_telegram_chat(self, chat):
    try:

        intent = classify_intent(chat["content"])

        if intent == "OPEN_ENDED":
            
            prompt_1 = build_prompt_1(
                CUSTOMER_MESSAGE=chat["content"],
                WORKFLOW_DESCRIPTION = global_variables.WORKFLOW_DESCRIPTION,
                PREVIOUS_QUESTION_BY_LLM = global_variables.PREVIOUS_QUESTION_BY_LLM,
                SLOT_ENTITY_LAST_STATE = global_variables.SLOT_ENTITY_LAST_STATE,
            )

            time.sleep(0.2)
            germini_response_1 = generate_answer_for_workflow(prompt_1)

            germini_response_1 = parse_llm_response(germini_response_1) 

            if isinstance(germini_response_1, str):
                context = kb_collection_store.knowledge_base_collection.query(
                    query_texts=[germini_response_1],
                    n_results=5,
                    include=["documents", "metadatas"]
                )

                time.sleep(0.2)
                germini_response_2 = generate_answer_for_enquiry_questions(
                    germini_response_1,
                    context["documents"][0]
                )

                send_message_over_telegram(germini_response_2, chat["sender_id"])
            else:

                global_variables.SLOT_ENTITY_LAST_STATE = germini_response_1

                prompt_2 = build_prompt_2(
                     CUSTOMER_MESSAGE=chat["sender_id"],
                     WORKFLOW_DESCRIPTION=global_variables.WORKFLOW_DESCRIPTION,
                     SLOT_ENTITY_LAST_STATE=global_variables.SLOT_ENTITY_LAST_STATE
                )
                if has_empty_field(global_variables.SLOT_ENTITY_LAST_STATE):

                    time.sleep(0.2)
                    germini_response_3 = generate_answer_for_workflow(prompt_2)
                    global_variables.PREVIOUS_QUESTION_BY_LLM = germini_response_3
                    send_message_over_telegram(germini_response_3, chat["sender_id"])
                else:
                    """Execute workflow"""
                    
                    executor = WorkflowExecutor(global_variables.WORKFLOW, chat["phone"])

                    final_context = executor.execute()


                    prompt = f"""
                        Write a message telling the customer that the request:
                        "{global_variables.WORKFLOW_DESCRIPTION}" was done successfully.
                        This response does not need to be professional with title and ending like
                        "Yours sincerely". It should be just a regular message in a conversation.

                        Example "Your password reset was done successfully. Is there anything 
                        else I could help with?"
                    """


                    time.sleep(0.2)
                    germini_response_4 = generate_answer_for_workflow(prompt)
                    send_message_over_telegram(germini_response_4, chat["sender_id"])

        else:
            global_variables.WORKFLOW = WORKFLOW_MAP.get(intent)            
            global_variables.CUSTOMER_MESSAGE = chat["content"]
            global_variables.WORKFLOW_DESCRIPTION = global_variables.WORKFLOW["description"]
            global_variables.SLOT_ENTITY_LAST_STATE = global_variables.WORKFLOW["slots"]
            prompt_3 = build_prompt_3(
                WORKFLOW_DESCRIPTION=global_variables.WORKFLOW["description"],
                SLOT_ENTITY_LAST_STATE=global_variables.WORKFLOW["slots"]
            )

            time.sleep(0.2)
            germini_response_5 = generate_answer_for_workflow(prompt_3)
            global_variables.PREVIOUS_QUESTION_BY_LLM = germini_response_5
            send_message_over_telegram(germini_response_5, chat["sender_id"])

    except Exception as e:
        print(f"chat io chat process failed with exceptions: {e}")

    