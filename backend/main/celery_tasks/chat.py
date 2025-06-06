from celery import shared_task
from google import genai
from decouple import config
from main.lib.intent_classifier import classify_intent
from main.lib import kb_collection_store

def generate_answer(query, context):
    """Generate response summary"""
    prompt = f"""Answer the question based on the context below.
    If the answer isn't contained in the context, say "I don't know."

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


@shared_task(bind=True, queue="io_tasks")
def handle_telegram_chat(self, chat):
    try:
        from main.lib.telegram_client import telegram_client_wrapper_instance
        reply_text = ""

        intent = classify_intent(chat["content"])
        # print("============ intent ==============> ", intent)

        if intent == "OPEN_ENDED":
            print("---------- this is open ended ----------> ")
            context = kb_collection_store.knowledge_base_collection.query(
                    query_texts=[chat["content"]],
                    n_results=5,
                    include=["documents", "metadatas"]
            )
            # reply_text = context["documents"][0][0]
            print(context["documents"][0][0])
            reply_text = generate_answer(chat["content"], context["documents"][0])

        else:
            print("---------- call a workflow ----------")
            pass


        if telegram_client_wrapper_instance:
            telegram_client_wrapper_instance.queue_message(
                recipient=chat["sender_id"],
                message=reply_text
            )
    except Exception as e:
        print(f"chat io chat process failed with exceptions: {e}")

    