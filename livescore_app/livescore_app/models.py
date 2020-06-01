from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.

def get_absolute_url(self):
          return reverse("player",kwargs={"player_id" : self.id})
User.add_to_class("get_absolute_url",get_absolute_url)  #add getabsolute url function to django user

# class Player(models.Model):
#     # every nickname must be unique for user identification
#     nickname = models.CharField(max_length=12, unique=True, primary_key=True)
#     firstName = models.CharField(max_length=30)
#     lastName = models.CharField(max_length=30)
#     dateOfBirth = models.DateField()
#     email = models.EmailField()
#     pass
#     def __str__(self):          # to change from Player object (1) to nickname  in admin panel
#         return self.nickname


class Tournament(models.Model):

    name= models.CharField(max_length=30)
    venue = models.CharField(max_length=30)
    date = models.DateField()
    maxPlayers = models.IntegerField()
    participants = models.ManyToManyField(User)

    # to change from Tournament object (1) to name of the tournament in admin panel
    def __str__(self):
        return self.name

    def openSpaces(self):
        return self.maxPlayers - self.participants.count()

    def get_absolute_url(self):
        return reverse("tournament",kwargs={"tournament_id" : self.id})

    
  
class Game(models.Model):

    STATUS_CODES = (
        ('1', 'not started'),
        ('2', 'running'),
        ('3', 'complete'),
    )

    tournament = models.ForeignKey(Tournament,on_delete=models.CASCADE)
    player1 = models.ForeignKey(User,related_name='player1',on_delete=models.CASCADE)
    player2 = models.ForeignKey(User,related_name='player2',on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUS_CODES, default='1')
    player1_score = models.IntegerField(default=0)
    player2_score = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse("game",kwargs={"game_id" : self.id})

    # to change from Game object (1) to name of the tournament : player1 nickname vs player2 nickname in admin panel
    def __str__(self):          
        return self.tournament.name + ', ' + self.player1.username + ' vs. ' + self.player2.username
    
