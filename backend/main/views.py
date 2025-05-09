from rest_framework.views import APIView
from rest_framework.response import Response
from decouple import config
from .lib import telegram_client
from rest_framework import status
from decouple import config






class TelegramView(APIView):

    def get(self, request):
        tg = telegram_client.TelegramClientWrapper()
        # tg.send_message_sync('me', 'Hello, myself!')
        # tg.send_message_sync('@unyimeudoh2', 'Hello, from unyime sim 1')
        tg.send_message_sync(config('CUSTOMER_PHONE'), 'Hello, from unyime sim 1')
        # res = tg.add_contact_sync(config('CUSTOMER_PHONE'), "unyime sim 2", "udoh")


        return Response({"message": "successful"}, status=status.HTTP_200_OK)


