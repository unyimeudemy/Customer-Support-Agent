
from rest_framework.views import APIView
from rest_framework.response import Response
from decouple import config
from .lib import telegram_client, redis_client
from rest_framework import status
from rest_framework.decorators import api_view
from .lib.omni_channel_message import OmniChannelMessage1
from datetime import datetime
from django.core.mail import send_mail
import asyncio
import logging
from main.lib.gmail_client import (
       send_plain_text_email,
       send_template_email
)
from main.template.email_template import html_template, order_mail_template
from main.lib.redis_client import redisClient, get_queue_count

logging.getLogger('chromadb').setLevel(logging.WARNING)


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
def add_new_task(request):
        print("=============== 1 ===============")
        # redis_client.add_task_to_incoming_q(message_1)
        try:

                SMTP_USER = "unyimeudemy20@gmail.com"
                SMTP_PASSWORD = config("GMAIL_APP_PASSWORD")

                # send_plain_text_email(
                #         subject="Plain Text Test",
                #         body="This is a simple plain text email.",
                #         from_email=SMTP_USER,
                #         to_email="unyimeudoh20@gmail.com",
                #         smtp_user=SMTP_USER,
                #         smtp_password=SMTP_PASSWORD
                # )

                # Send HTML email using template


                send_template_email(
                        subject="Welcome to Our App",
                        template_str=order_mail_template,
                        context_dict={"name": "Unyime"},
                        from_email=SMTP_USER,
                        to_email="unyimeudoh20@gmail.com",
                        smtp_user=SMTP_USER,
                        smtp_password=SMTP_PASSWORD
                )

        except Exception as e:
               print(e)
               
        return Response({"message": "successful"}, status=status.HTTP_200_OK)

@api_view(['GET'])
def add_task_to_processing(request):
        print("=============== 2 ===============")
        # asyncio.run(redis_client.move_task_from_incoming_q_to_processing_hash())
        return Response({"message": "successful"}, status=status.HTTP_200_OK)

@api_view(['GET'])
def add_task_to_done(request):
        print("=============== 3 ===============")
        # asyncio.run(redis_client.move_task_from_processing_hash_to_done_hash("unyimeudoh2"))
        return Response({"message": "successful"}, status=status.HTTP_200_OK)

@api_view(['GET'])
def empty_redis_queue_and_list(request):
        redisClient.delete("incoming_tasks")
        redisClient.delete("processing_tasks")
        redisClient.delete("done_tasks")
        print("==incoming  ==> ", get_queue_count())
        return Response({"message": "successful"}, status=status.HTTP_200_OK)


