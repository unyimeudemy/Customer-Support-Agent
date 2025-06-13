import redis
import json
from .omni_channel_message import OmniChannelMessage1
from channels.layers import get_channel_layer

redisClient = redis.Redis(host='localhost', port=6379, decode_responses=True)
channel_layer = get_channel_layer()


processing_arr = []
done_arr = []

async def add_task_to_incoming_q(message_obj: OmniChannelMessage1):
    """
    ensure that task is not already in the incoming task before 
    adding it
    """
    if not redisClient.sismember("incoming_tasks_set", message_obj.sender_id):
        redisClient.sadd("incoming_tasks_set", message_obj.sender_id)
        redisClient.rpush("incoming_tasks", json.dumps(message_obj.__dict__))
        await channel_layer.group_send(
            "unprocessed_customer_queue",
            {
                "type": "queue.update",
                "data" : message_obj.__dict__,
            }
        )

async def move_task_from_incoming_q_to_processing_hash():
    task_str = redisClient.lpop("incoming_tasks")
    if task_str:
        task = json.loads(task_str)
        sender_id = task.get("sender_id")
        if sender_id:
            redisClient.srem("incoming_tasks_set", sender_id)
            redisClient.hset("processing_tasks", sender_id, json.dumps(task))
            await channel_layer.group_send(
                "currently_processed_customer_list",
                {
                    "type": "list.update",
                    "data" : task,
                }
            )

async def move_task_from_processing_hash_to_done_hash(sender_id: str):
    task_str = redisClient.hget("processing_tasks", sender_id)
    if task_str:
        task = json.loads(task_str)
        if sender_id:
            if not redisClient.sismember("done_tasks_set", sender_id):
                redisClient.sadd("done_tasks_set", sender_id)
                redisClient.rpush("done_tasks", sender_id, task_str)
            redisClient.hdel("processing_tasks", sender_id)
            await channel_layer.group_send(
                "processed_customer_list",
                {
                    "type": "list.update",
                    "data": task
                }
            )


def get_queue_count():
    return {
        "incoming": redisClient.llen("incoming_tasks"),
        "processing": redisClient.hlen("processing_tasks"),
        "done": redisClient.llen("done_tasks"),
    }

def get_queue_status():
    incoming = redisClient.lrange("incoming_tasks", 0, -1)
    processing = redisClient.hgetall("processing_tasks", 0, -1)
    done = redisClient.lrange("done_tasks", 0, -1)

    return {
        "incoming": [json.loads(task) for task in incoming],
        "processing": [json.loads(v.decode()) for v in processing.values()],
        "done": [json.loads(task) for task in done],
    }


# await channel_layer.group_send(
#     "queue_updates",
#     {
#         "type": "queue.update",
#         "data": {
#             "action": "incoming_added",
#             "task": message_obj.__dict__,
#         }
#     }
# )