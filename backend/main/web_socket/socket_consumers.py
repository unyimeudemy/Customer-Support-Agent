from channels.generic.websocket import AsyncWebsocketConsumer
import json

class UnprocessedCustomerConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("unprocessed_customer_queue", self.channel_name)
        await self.accept()
    
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("unprocessed_customer_queue", self.channel_name)

    async def queue_update(self, event):
        await self.send(text_data=json.dumps(event["data"]))



class CurrentlyProcessedCustomerConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("currently_processed_customer_list", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("currently_processed_customer_list", self.channel_name)

    async def list_update(self, event):
        await self.send(text_data=json.dumps(event["data"]))


class ProcessedCustomerConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("processed_customer_list", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("processed_customer_list", self.channel_name)
    
    async def list_update(self, event):
        await self.send(text_data=json.dumps(event["data"]))