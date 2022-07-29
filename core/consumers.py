from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync
import json
from .models import Group, Chat
from channels.db import database_sync_to_async


# WebsocketConsumer
class MyWebsocketConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.group_name = self.scope['url_route']['kwargs']['gname']
        async_to_sync(self.channel_layer.group_add)(self.group_name, self.channel_name)
        print("connected")
    
    def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        # find the group
        group = Group.objects.get(name=self.group_name)
        if self.scope['user'].is_authenticated:
            # save chat
            message = data['msg']
            chat = Chat.objects.create(content=message, group=group)
            async_to_sync(self.channel_layer.group_send)(self.group_name, {
                    'type': 'chat.message',
                    'message': message
                })        
        else:
            self.send(text_data=json.dumps({
            'msg':'You are not authenticated.'
            }))
            raise StopConsumer()

    # handeller function
    def chat_message(self, event):
        self.send( text_data=json.dumps({
            'msg': event['message']
        }))

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(self.group_name, self.channel_name)
        print("disconnected", close_code)
        raise StopConsumer()
     

# AsyncWebsocketConsumer
class MyAsyncWebsocketConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        self.group_name = self.scope['url_route']['kwargs']['gname']
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        print("connected")
    
    async def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        # find the group
        group = await database_sync_to_async(Group.objects.get)(name=self.group_name)
        if self.scope['user'].is_authenticated:
            message = data['msg']
            # create a chat
            chat = await database_sync_to_async(Chat.objects.create)(content=message, group=group)
            await self.channel_layer.group_send(self.group_name, {
                    'type': 'chat.message',
                    'message': message
                })        
        else:
            await self.send(text_data=json.dumps({
                'msg':'You are not authenticated.'
            }))
            raise StopConsumer()

    # handeller function
    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            'msg': event['message']
        }))
        
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)
        print("disconnected", close_code)
        raise StopConsumer()
     
