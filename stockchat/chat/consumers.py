from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer, WebsocketConsumer
import json

from .service import ReplyService
from .models import ChatMessage


class ChatConsumer(WebsocketConsumer):

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        chat_message = ChatMessage(text_data_json['user'], text_data_json['message'])

        async_to_sync(self.channel_layer.group_send)(self.room_group_name, chat_message.__dict__)

        reply = ReplyService.get_reply_for(chat_message)

        if reply:
            async_to_sync(self.channel_layer.group_send)(self.room_group_name, reply.__dict__)

    # Receive message from room group
    def chat_message(self, event):
        chat_message = ChatMessage(event['user'], event['message'])

        # Send message to WebSocket
        self.send(text_data=json.dumps(chat_message.__dict__))
