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
            print("---------- call a workflow ----------" )
            workflow = WORKFLOW_MAP.get(intent)
            # final_context = workflow_executor(workflow, chat["phone"])
            executor = WorkflowExecutor(workflow, chat["phone"])
            final_context = executor.execute()
            print("final context: ", final_context)


    except Exception as e:
        print(f"chat io chat process failed with exceptions: {e}")

    