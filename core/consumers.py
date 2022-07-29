from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
# from channels.exceptions import StopConsumer
# from asgiref.sync import async_to_sync
# import json
# from .models import Group, Chat
# from channels.db import database_sync_to_async


# WebsocketConsumer
class MyWebsocketConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        print("connected")
    
    def receive(self, text_data=None, bytes_data=None):
        print("received", text_data)
        self.send(text_data="Message from server")
        
    def disconnect(self, close_code):
        print("disconnected", close_code)
     
