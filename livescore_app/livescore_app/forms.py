from django import forms

from .models import Game

class GameCreateForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['player1', 'player2','status']