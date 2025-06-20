import asyncio
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agent.settings')
django.setup()

from main.lib import telegram_client


async def main():
    wrapper = telegram_client.TelegramClientWrapper()
    telegram_client.telegram_client_wrapper_instance = wrapper
    await wrapper.start()


if __name__ == "__main__":
    asyncio.run(main())

