import redis
import json
from .omni_channel_message import OmniChannelMessage1

redisClient = redis.Redis(host='localhost', port=6379, decode_responses=True)
processing_arr = []
done_arr = []

def add_task_to_incoming_q(message_obj: OmniChannelMessage1):
    redisClient.rpush("incoming_tasks", json.dumps(message_obj.__dict__))

def move_task_from_incoming_q_to_processing_hash():
    task_str = redisClient.lpop("incoming_tasks")
    if task_str:
        task = json.loads(task_str)
        message_id = task.get("message_id")
        if message_id:
            redisClient.hset("processing_tasks", message_id, json.dump(task))
        return task
    return None

def move_task_from_processing_hash_to_done_hash(message_id: str):
    task_str = redisClient.hget("processing_tasks", message_id)
    if task_str:
        redisClient.hset("done_tasks", message_id, task_str)
        redisClient.hdel("processing_tasks", message_id)
        return json.loads(task_str)
    return None

def get_queue_count():
    return {
        "incoming": redisClient.llen("incoming_tasks"),
        "processing": redisClient.llen("processing_tasks"),
        "done": redisClient.llen("done_tasks"),
    }

def get_queue_status():
    incoming = redisClient.lrange("incoming_tasks", 0, -1)
    processing = redisClient.lrange("processing_tasks", 0, -1)
    done = redisClient.lrange("done_tasks", 0, -1)

    return {
        "incoming": [json.loads(task) for task in incoming],
        "processing": [json.loads(task) for task in processing],
        "done": [json.loads(task) for task in done],
    }