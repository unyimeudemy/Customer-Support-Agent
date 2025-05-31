from django.apps import AppConfig
from .lib import telegram_client
import asyncio
import threading

# from transformers import AutoTokenizer
# from pathlib import Path
# import urllib.request


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    def ready(self):
        def start_telegram():
            try:
                wrapper = telegram_client.TelegramClientWrapper()
                telegram_client.telegram_client_wrapper_instance = wrapper
                asyncio.run(wrapper.start())
            except Exception as e:
                print(f"Error starting Telegram client: {e}")

        thread = threading.Thread(target=start_telegram, daemon=True)
        thread.start()


        # base_dir = Path(__file__).resolve().parent.parent
        # embeddings_dir = base_dir / 'embedded_onnx'
        # tokenizer_dir = embeddings_dir / 'tokenizer'

        # if not embeddings_dir.exists():
        #     embeddings_dir.mkdir()


        # # Download tokenizer if not present
        # if not tokenizer_dir.exists():
        #     print("Downloading tokenizer...")
        #     tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
        #     tokenizer.save_pretrained(tokenizer_dir)