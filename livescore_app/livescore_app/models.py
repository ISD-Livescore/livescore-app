from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.


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

    def __str__(self):          # to change from Tournament object (1) to name of the tournament in admin panel
        return self.name

    def openSpaces(self):
        return self.maxPlayers - self.participants.count()

    def get_absolute_url(self):
        return reverse("tournament",kwargs={"my_id" : self.id})
    
  
class Game(models.Model):
    tournament = models.ForeignKey(Tournament,on_delete=models.CASCADE)
    player1 = models.ForeignKey(User,related_name='player1',on_delete=models.CASCADE)
    player2 = models.ForeignKey(User,related_name='player2',on_delete=models.CASCADE)

    def __str__(self):          # to change from Game object (1) to name of the tournament : player1 nickname vs player2 nickname in admin panel
        return self.tournament.name + ', ' + self.player1.nickname + ' vs. ' + self.player2.nickname
    
