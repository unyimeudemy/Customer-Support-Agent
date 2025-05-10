import redis
import json

redisClient = redis.Redis(host='localhost', port=6379, decode_responses=True)

def add_task_to_incoming_q(user_id, message_id):
    task = {'user_id': user_id, 'message_id': message_id}
    redisClient.rpush("incoming_tasks", json.dumps(task))


def move_task_from_incoming_q_to_processing_q():
    task = redisClient.lpop("incoming_tasks")
    if task:
        redisClient.rpush("processing_tasks", task)
        return json.loads(task)
    return None


def move_task_from_processing_q_to_done_q():
    task = redisClient.lpop("processing_tasks")
    # redisClient.lrem("processing_tasks", 0, json.dumps(task))
    if task:
        redisClient.rpush("done_tasks", json.dumps(task))


def empty_a_queue(queuename: str):
    redisClient.delete(queuename)



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