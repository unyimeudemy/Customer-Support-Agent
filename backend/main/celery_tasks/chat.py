from celery import shared_task
from google import genai
from decouple import config



@shared_task(bind=True, queue="io_tasks")
def handle_telegram_chat(self, chat):
    try:
        from main.lib.telegram_client import telegram_client_wrapper_instance

        client = genai.Client(api_key=config('GEMINI_API_KEY'))
        response = client.models.generate_content(
            model="gemini-2.0-flash", contents=chat["content"]
        )
        reply_text = response.text
        print("****** human ****** ", chat["content"])
        print("****** germini ****** " + reply_text)

        if telegram_client_wrapper_instance:
            telegram_client_wrapper_instance.queue_message(
                recipient=chat["sender_id"],
                message=reply_text
            )
    except Exception as e:
        print(f"chat io chat process failed with exceptions: {e}")

    