
from rest_framework.views import APIView
from rest_framework.response import Response
from decouple import config
from .lib import telegram_client, redis_client
from rest_framework import status
from .lib import redis_client
from rest_framework.decorators import api_view
from .lib.omni_channel_message import OmniChannelMessage1
from datetime import datetime
import asyncio
import logging
# from sklearn.metrics.pairwise import cosine_similarity


logging.getLogger('chromadb').setLevel(logging.WARNING)

# import logging
# logging.getLogger("transformers").setLevel(logging.ERROR)
# logging.getLogger("chromadb").setLevel(logging.ERROR)
# logging.getLogger("onnxruntime").setLevel(logging.ERROR)



class TelegramView(APIView):

    def get(self, request):
        tg = telegram_client.TelegramClientWrapper()
        # tg.send_message_sync('me', 'Hello, myself!')
        # tg.send_message_sync('@unyimeudoh2', 'Hello, from unyime sim 1')
        tg.send_message_sync(config('CUSTOMER_PHONE'), 'Hello, from unyime sim 1')
        # res = tg.add_contact_sync(config('CUSTOMER_PHONE'), "unyime sim 2", "udoh")
        # res = redis_client.redisClient.get('name')
        return Response({"message": "successful"}, status=status.HTTP_200_OK)



# Example data
channel_data = "telegram"
content_data = "Hello, how can I help?"
sender_id_data = "unyimeudoh2"
sender_name_data = "unyime sim 2 udoh"
parsed_timestamp = datetime.utcnow()

# Create the instance
message_1 = OmniChannelMessage1(
    channel=channel_data,
    content=content_data,
    sender_id=sender_id_data,
    sender_name=sender_name_data,
    timestamp=parsed_timestamp
)

@api_view(['GET'])
def add_new_task(request):
        print("=============== 1 ===============")
        print(redis_client.get_queue_count())
        redis_client.add_task_to_incoming_q(message_1)
        print(redis_client.get_queue_count())
        return Response({"message": "successful"}, status=status.HTTP_200_OK)

@api_view(['GET'])
def add_task_to_processing(request):
        print("=============== 2 ===============")
        # print(redis_client.get_queue_count())
        asyncio.run(redis_client.move_task_from_incoming_q_to_processing_hash())
        
        # print(redis_client.get_queue_count())

        # try:
        #         knowledge_base_collection.add(
        #                 documents=[
        #                         "To reset your password, click the 'Forgot Password' link on the login page.",
        #                         "Our customer support is available 24/7 via chat or phone."
        #                 ],
        #                 ids=["doc1", "doc2"],
        #         )
        #         return Response({"message": "successful"}, status=200)
        # except Exception as e:
        #         print({"error": str(e)})

        return Response({"message": "successful"}, status=status.HTTP_200_OK)

@api_view(['GET'])
def add_task_to_done(request):
        print("=============== 3 ===============")
        # print(redis_client.get_queue_count())
        asyncio.run(redis_client.move_task_from_processing_hash_to_done_hash("unyimeudoh2"))
        # redis_client.empty_a_queue('done_tasks')
        # print(redis_client.get_queue_count())

        # try:
                # results = knowledge_base_collection.query(
                #         query_texts=["will there be someone to help with it tommorow?"],
                #         n_results=1,
                #         include=["documents", "metadatas"]
                # )
        #         print("---------------------> ", results)
        #         return Response({"message": "successful"}, status=200)
        # except Exception as e:
        #         print({"error": str(e)})
        
        return Response({"message": "successful"}, status=status.HTTP_200_OK)
