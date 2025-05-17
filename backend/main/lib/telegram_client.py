from telethon import TelegramClient, events
import asyncio
import os
from telethon.sessions import StringSession
from telethon.tl.types import InputPhoneContact
from telethon.tl import functions, types
from telethon.tl.functions.contacts import ImportContactsRequest
import json
from datetime import datetime
from decouple import config
from .omni_channel_message import OmniChannelMessage1
from .redis_client import add_task_to_incoming_q


class TelegramClientWrapper():

    def __init__(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        self.api_id = int(config('TELEGRAM_API_ID'))
        self.api_hash = config('TELEGRAM_API_HASH')
        self.session_string = config('TELEGRAM_SESSION_STRING')

        self.client = TelegramClient(
            StringSession(self.session_string),
            self.api_id,
            self.api_hash
        )

    async def send_message(self, recipient, message):
        async with self.client:
            await self.client.send_message(recipient, message)

    def send_message_sync(self, recipient, message):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.send_message(recipient, message))

    async def add_contact(self, phone_number, first_name, last_name):
        async with self.client:
            contact = InputPhoneContact(client_id=0, phone=phone_number, first_name=first_name, last_name=last_name)
            result = await self.client(ImportContactsRequest([contact]))
            result_dict = result.to_dict()
            return result_dict            

    def add_contact_sync(self, phone_number, first_name, last_name):
        loop = asyncio.get_event_loop()
        return loop.run_until_complete(self.add_contact(phone_number, first_name, last_name))   

    async def add_multiple_contacts(self, contacts_list):
        async with self.client:
            contacts = []
            for contact in contacts_list:
                contacts.append(InputPhoneContact(
                    client_id=0,
                    phone=contact['phone'],
                    first_name=contact['first_name'],
                    last_name=contact['last_name']
                ))

            result = await self.client(ImportContactsRequest(contacts))
            result_dict = result.to_dict()
            return result_dict

    def add_multiple_contacts_sync(self, contacts_list):
        loop = asyncio.get_event_loop()
        return loop.run_until_complete(self.add_multiple_contacts(contacts_list))

    async def handle_new_message(self, event):
        user = await event.get_sender()
        message = event.message.text  
        full_name = f"{user.first_name or ''} {user.last_name or ''}".strip()
        timestamp = event.message.date.isoformat()
        chat = OmniChannelMessage1(
            channel="telegram",
            sender_id=user.username or "unknown",
            sender_name=full_name,
            timestamp=timestamp,
            content=message
        )
        await add_task_to_incoming_q(chat)

    async def start(self):
        await self.client.start()

        # Register all event handlers
        self.client.add_event_handler(self.handle_new_message, events.NewMessage())

        print("awaiting new message")
        await self.client.run_until_disconnected()