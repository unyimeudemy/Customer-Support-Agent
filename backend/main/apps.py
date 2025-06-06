from django.apps import AppConfig
from .lib import telegram_client
import asyncio
import threading
import os



class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    def ready(self):
        os.environ["TOKENIZERS_PARALLELISM"] = "false"


        from main.vector.chroma_client import setup_chroma_client
        setup_chroma_client()

        def start_telegram():
            try:
                wrapper = telegram_client.TelegramClientWrapper()
                telegram_client.telegram_client_wrapper_instance = wrapper
                asyncio.run(wrapper.start())
            except Exception as e:
                print(f"Error starting Telegram client: {e}")

        thread = threading.Thread(target=start_telegram, daemon=True)
        thread.start()


