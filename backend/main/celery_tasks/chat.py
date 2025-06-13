from celery import shared_task
from google import genai
from decouple import config
from main.lib.intent_classifier import classify_intent
from main.lib import kb_collection_store
from main.lib.workflow_map import WORKFLOW_MAP
from main.lib.workflow_executor  import WorkflowExecutor

def generate_answer(query, context):
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
        from main.lib.telegram_client import telegram_client_wrapper_instance
        reply_text = ""

        intent = classify_intent(chat["content"])

        if intent == "OPEN_ENDED":
            print("---------- this is open ended ----------> ")

            germini_response = """
                ### Background intro:
                you are a customer service agent and this statement '[customer_message]'
                is part of an ongoing converstation to enable the user carry out the action
                of [workflow_describtion]. 
            
                ### Condition 1: 
                If the statement [customer_message] is entirely unrelated to the statement 
                [previous_slot_filling_question_by_llm], which means that it is most likely
                another question that is totally unrelated to the context [workflow_describtion]
                and the request [previous_slot_filling_question_by_llm]
                

                ### Condition 2
                But if the  statement [customer_message] answers the question [previous_slot_filling_question_by_llm],
                use this word or group of words to update the json [slot_entity_last_state].

                Also if the statement [customer_message] is a single word or group of words 
                that do not form a valid english statement that is either correct or incorrect grammatically, 
                then it a valid answer so you should use it to update a field in [slot_entity_last_state]
                that the statement [previous_slot_filling_question_by_llm] was trying to get a value for.

                
                ### Answer:
                if the statement [customer_message] feel under condition 1 
                return only the statement [customer_message] without adding anything to it.

                But if the question the statement [customer_message] feel under condition 2
                return the updated [slot_entity_last_state] json alone and nothing else with it.

                """
            

            if isinstance(germini_response, str):
                context = kb_collection_store.knowledge_base_collection.query(
                        query_texts=[chat["content"]],
                        n_results=5,
                        include=["documents", "metadatas"]
                )

                reply_text = generate_answer(chat["content"], context["documents"][0])
                if telegram_client_wrapper_instance:
                    telegram_client_wrapper_instance.queue_message(
                        recipient=chat["sender_id"],
                        message=reply_text
                    )
            else:
                pass
                """
                    ### Background intro:
                    you are a customer service agent and this statement '[customer_message]'
                    is part of an ongoing converstation to enable the user carry out the action
                    of [workflow_describtion].

                    The goal is for the user to provide all the information still missing in the target json:
                    [slot_entity_last_state]. Ask the user kindly to provide one of the missing 
                    information in [slot_entity_last_state]. Your request should be something 
                    like this "Kindly provide your [one of the fields from target json]". 

                    Adjust the statement "Kindly provide your [one of the fields from target json]"
                    as appropriate to suit the field you are requesting.

                """

        else:
            print("---------- call a workflow ----------" )
            workflow = WORKFLOW_MAP.get(intent)
            # final_context = workflow_executor(workflow, chat["phone"])
            executor = WorkflowExecutor(workflow, chat["phone"])
            final_context = executor.execute()
            print("final context: ", final_context)
            """
            you are a customer service agent and a customer has just requested to carry
            out this process: [workflow describtion]. you will need the following details 
            [workflow slot] but the customer just mentioned this request and hasn't 
            provided the information yet. Ask the customer kindly to provide the value for 
            first field here [workflow slot].

            Then set a field called context_topic in the global context variable to the 
            current context.
            
            """


    except Exception as e:
        print(f"chat io chat process failed with exceptions: {e}")

    