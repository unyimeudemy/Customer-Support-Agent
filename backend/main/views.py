from rest_framework.views import APIView
from rest_framework.response import Response
from decouple import config
from .lib import telegram_client, redis_client
from rest_framework import status
from .lib import redis_client
from rest_framework.decorators import api_view




class TelegramView(APIView):

    def get(self, request):
        tg = telegram_client.TelegramClientWrapper()
        # tg.send_message_sync('me', 'Hello, myself!')
        # tg.send_message_sync('@unyimeudoh2', 'Hello, from unyime sim 1')
        tg.send_message_sync(config('CUSTOMER_PHONE'), 'Hello, from unyime sim 1')
        # res = tg.add_contact_sync(config('CUSTOMER_PHONE'), "unyime sim 2", "udoh")
        # res = redis_client.redisClient.get('name')
        return Response({"message": "successful"}, status=status.HTTP_200_OK)


    


@api_view(['GET'])
def add_task_to_done(request):
        print("=============== 3 ===============")
        print(redis_client.get_queue_count())
        redis_client.move_task_from_processing_q_to_done_q()
        # redis_client.empty_a_queue('done_tasks')
        print(redis_client.get_queue_count())
        return Response({"message": "successful"}, status=status.HTTP_200_OK)


@api_view(['GET'])
def add_new_task(request):
        print("=============== 1 ===============")
        print(redis_client.get_queue_count())
        redis_client.add_task_to_incoming_q("1", "This is a task")
        print(redis_client.get_queue_count())
        return Response({"message": "successful"}, status=status.HTTP_200_OK)

@api_view(['GET'])
def add_task_to_processing(request):
    print("=============== 2 ===============")
    print(redis_client.get_queue_count())
    redis_client.move_task_from_incoming_q_to_processing_q()
    print(redis_client.get_queue_count())
    return Response({"message": "successful"}, status=status.HTTP_200_OK)