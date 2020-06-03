import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.shortcuts import get_object_or_404
from livescore_app.models import Game

class GameConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['game_id']
        self.room_group_name = 'game_%s' % self.room_name

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

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        player1Score = text_data_json['player1Score']
        player2Score = text_data_json['player2Score']
        gameId = text_data_json['gameId']

        game = get_object_or_404(Game, id=gameId)
        game.player1_score = player1Score
        game.player2_score = player2Score

        if player1Score >= 21 or player2Score >= 21:
            game.status = '3' 
        elif player1Score > 0 or player2Score > 0:
            game.status = '2'
        
        game.save()

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'score_message',
                'player1Score': player1Score,
                'player2Score': player2Score
            }
        )

    def score_message(self, event):
        player1Score = event['player1Score']
        player2Score = event['player2Score']

        self.send(text_data=json.dumps({
            'player1Score': player1Score,
            'player2Score': player2Score
        }))
