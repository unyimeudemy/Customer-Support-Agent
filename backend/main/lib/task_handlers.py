from .omni_channel_message import OmniChannelMessage1
from .redis_client import (
    add_task_to_incoming_q,
    move_task_from_incoming_q_to_processing_hash,
    move_task_from_processing_hash_to_done_hash,
    redisClient
)
from main.celery_tasks.emails import (
    handle_failed_order_email,
    generate_report,
)
from agent.celery import (
    io_active_len,
    io_reserved_len,
    cpu_active_len,
    cpu_reserved_len
)
from celery.signals import task_prerun, task_postrun
import asyncio
from .channels_conversation import (
    handle_telegram_conversation,
    handle_gmail_conversation,
    handle_whatsapp_conversation
)


def choose_channel_handler(chat: OmniChannelMessage1):
    if chat.channel == "telegram":
        handle_telegram_conversation(chat)
    if chat.channel == "email":
        handle_gmail_conversation(chat)
    if chat.channel == "whatsapp":
        handle_whatsapp_conversation(chat)


async def incoming_tasks_handler(chat: OmniChannelMessage1):
    if (
        not redisClient.sismember("incoming_tasks_set", chat.sender_id)
        and not redisClient.hexists("processing_tasks", chat.sender_id)
    ):
        
        await add_task_to_incoming_q(chat)
        if io_active_len < 5:
            await move_task_from_incoming_q_to_processing_hash()
            choose_channel_handler(chat)
        # handle_failed_order_email.delay(chat.__dict__)
        # generate_report.delay(chat.__dict__)
    elif not redisClient.hexists("processing_tasks", chat.sender_id):
        choose_channel_handler(chat)
    else:
        pass
        
  
@task_postrun.connect
def on_task_done(args=None, **_): 
    print("------- celery done -------------")
    if args:
        task_input = args[0]
        sender_id = task_input.get("sender_id") if isinstance(task_input, dict) else None
        print(f"Sender ID from task args: {sender_id}")

    asyncio.run(move_task_from_processing_hash_to_done_hash(sender_id))


