import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from create_chat.models import CreateChat
from .models import Chat

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_id  = self.scope["url_route"]["kwargs"]["uuid"]
        self.room_group_name = f"chat_{self.room_id}"

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        user = text_data_json["user"]
        chatroom = CreateChat.objects.get(id=self.room_id)
        if chatroom.chat_member_1 == user or chatroom.chat_member_2 == user:
            chat_db = Chat(chatroom=chatroom, user=user, text=message)
            chat_db.save()

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "chat.message", "message": message, "sender": user}
        )

    def chat_message(self, event):
        message = event["message"]
        sender = event["sender"]
        self.send(text_data=json.dumps({"message": message, "sender": sender}))
