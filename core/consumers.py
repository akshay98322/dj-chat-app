from channels.generic.websocket import \
            (WebsocketConsumer, 
            AsyncWebsocketConsumer, 
            JsonWebsocketConsumer, 
            AsyncJsonWebsocketConsumer )
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync
import json
from .models import Group, Chat
from channels.db import database_sync_to_async
from django.contrib.auth.models import User


# WebsocketConsumer
class MyWebsocketConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.group_name = self.scope['url_route']['kwargs']['gname']
        async_to_sync(self.channel_layer.group_add)(self.group_name, self.channel_name)
        print("connected")
    
    def receive(self, text_data=None, bytes_data=None):
        if self.scope['user'].is_authenticated:
            data = json.loads(text_data)
            # find the group
            group = Group.objects.get(name=self.group_name)
            # get user
            u_name = self.scope['user'].username
            user_obj = User.objects.get(username=u_name)
            # save chat
            message = data['msg']
            chat = Chat.objects.create(content=message, group=group, user=user_obj)
            async_to_sync(self.channel_layer.group_send)(self.group_name, {
                    'type': 'chat.message',
                    'message': message,
                    'user': u_name
                })        
        else:
            self.send(text_data=json.dumps({
            'msg':'You are not authenticated.',
            'user':'Anonymous'
            }))
            raise StopConsumer()

    # handeller function
    def chat_message(self, event):
        self.send(text_data=json.dumps({
            'msg': event['message'],
            'user': event['user']
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
        if self.scope['user'].is_authenticated:
            data = json.loads(text_data)
            # find the group
            group = await database_sync_to_async(Group.objects.get)(name=self.group_name)
            # get user
            u_name = self.scope['user'].username
            user_obj = await database_sync_to_async(User.objects.get)(username=u_name)
            # save chat
            message = data['msg']
            chat = await database_sync_to_async(Chat.objects.create)(content=message, group=group, user=user_obj)
            await self.channel_layer.group_send(self.group_name, {
                    'type': 'chat.message',
                    'message': message,
                    'user': u_name
                })        
        else:
            await self.send(text_data=json.dumps({
                'msg':'You are not authenticated.',
                'user':'Anonymous'
            }))
            raise StopConsumer()

    # handeller function
    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            'msg': event['message'],
            'user': event['user']
        }))
        
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)
        print("disconnected", close_code)
        raise StopConsumer()

# JsonWebsocketConsumer
class MyJsonWebsocketConsumer(JsonWebsocketConsumer):
    def connect(self):
        self.accept()
        self.group_name = self.scope['url_route']['kwargs']['gname']
        async_to_sync(self.channel_layer.group_add)(self.group_name, self.channel_name)
        print("connected")
    
    def receive_json(self, content, **kwargs):
        if self.scope['user'].is_authenticated:
            # find the group
            group = Group.objects.get(name=self.group_name)
            # get user
            u_name = self.scope['user'].username
            user_obj = User.objects.get(username=u_name)
            # save chat
            message = content['msg']
            chat = Chat.objects.create(content=message, group=group, user=user_obj)
            async_to_sync(self.channel_layer.group_send)(self.group_name, {
                    'type': 'chat.message',
                    'message': message,
                    'user': u_name
                })        
        else:
            self.send(text_data=json.dumps({
            'msg':'You are not authenticated.',
            'user':'Anonymous'
            }))
            raise StopConsumer()

    # handeller function
    def chat_message(self, event):
        self.send_json({
            'msg': event['message'],
            'user': event['user']
        })

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(self.group_name, self.channel_name)
        print("disconnected", close_code)
        raise StopConsumer()

# AsyncJsonWebsocketConsumer
class MyAsyncJsonWebsocketConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()
        self.group_name = self.scope['url_route']['kwargs']['gname']
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        print("connected")
    
    async def receive_json(self, content, **kwargs):
        if self.scope['user'].is_authenticated:
            # find the group
            group = await database_sync_to_async(Group.objects.get)(name=self.group_name)
            # get user
            u_name = self.scope['user'].username
            user_obj = await database_sync_to_async(User.objects.get)(username=u_name)
            # save chat
            message = content['msg']
            chat = await database_sync_to_async(Chat.objects.create)(content=message, group=group, user=user_obj)
            await self.channel_layer.group_send(self.group_name, {
                    'type': 'chat.message',
                    'message': message,
                    'user': u_name
                })        
        else:
            self.send(text_data=json.dumps({
            'msg':'You are not authenticated.',
            'user':'Anonymous'
            }))
            raise StopConsumer()

    # handeller function
    async def chat_message(self, event):
        await self.send_json({
            'msg': event['message'],
            'user': event['user']
        })

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)
        print("disconnected", close_code)
        raise StopConsumer()
