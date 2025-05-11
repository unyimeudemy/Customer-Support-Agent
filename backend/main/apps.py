from django.apps import AppConfig
from .lib import telegram_client
import asyncio
import threading

class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    def ready(self):
        def start_telegram():
            try:
                wrapper = telegram_client.TelegramClientWrapper()
                asyncio.run(wrapper.start())
            except Exception as e:
                print(f"Error starting Telegram client: {e}")

        thread = threading.Thread(target=start_telegram, daemon=True)
        thread.start()