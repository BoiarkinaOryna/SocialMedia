import json, datetime
from channels.generic.websocket import AsyncWebsocketConsumer
from .forms import MessageForm
from channels.db import database_sync_to_async
from .models import ChatGroup, ChatMessage

class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        print("1")
        self.room_group_name = f"{self.scope['url_route']['kwargs']['group_pk']}"
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
        await self.send(
            text_data= json.dumps({
                'type':'connection_established',
                'message':'connection_succsefull'
            })
        )
    async def receive(self, text_data):
        '''Отримуємо дані із форми повідомлення, та передаємо назад до клієнта,
        для відображення у чаті всіх повідомлень'''
        print("2")
        message = await self.save_message_to_db(text_data = text_data)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'send_message_to_every_member',
                'text_data': text_data,
                "author_username": self.scope["user"].username,
                'date_time' : message.date_time
            }
        )
    
    async def send_message_to_every_member(self, event):
        '''
        
        '''

        form = MessageForm(json.loads(event['text_data']))
        #
        try:
            #
            if form.is_valid():

                await self.send(text_data= json.dumps({
                    'type': 'chat', #
                    'message': form.cleaned_data['message'], #
                    'username': event["author_username"], #
                    'date_time': event['date_time'].isoformat()#
                }))
        except Exception as ERROR:
            print(ERROR)
    
    @database_sync_to_async
    def save_message_to_db(self, text_data: json):
        '''
            Цю функцію ми створили для того щоб зберігати наші повідомлення у базу даних
        '''
        print("3")
        return ChatMessage.objects.create(
            content = json.loads(text_data)['message'],
            author = self.scope['user'],
            chat_group = ChatGroup.objects.get(pk = self.room_group_name)
        )