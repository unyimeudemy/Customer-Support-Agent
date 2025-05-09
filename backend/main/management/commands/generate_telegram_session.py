from django.core.management.base import BaseCommand
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from decouple import config

class Command(BaseCommand):
    help = 'Generate a Telegram StringSession for use in .env'

    def handle(self, *args, **kwargs):
        api_id = int(config("TELEGRAM_API_ID"))
        api_hash = config("TELEGRAM_API_HASH")

        with TelegramClient(StringSession(), api_id, api_hash) as client:
            session_string = client.session.save()
            self.stdout.write(self.style.SUCCESS("🔑 Your session string:"))
            self.stdout.write(session_string)
