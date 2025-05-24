
from main.celery_tasks.chat import (
    handle_telegram_chat
)

from .omni_channel_message import OmniChannelMessage1


def handle_telegram_conversation(chat: OmniChannelMessage1):
    handle_telegram_chat.delay(chat.__dict__)
    

def handle_gmail_conversation(sender_id: str):
    pass

def handle_whatsapp_conversation(sender_id: str):
    pass