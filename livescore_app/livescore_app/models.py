from django.db import models
from django.urls import reverse

# Create your models here.

class Player(models.Model):
    nickname = models.CharField(max_length=12,unique=True,primary_key=True)  #every nickname must be unique for user identification
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    dateOfBirth = models.DateField()
    email = models.EmailField()
    pass

    

class Tournament(models.Model):
    name= models.CharField(max_length=30)
    venue = models.CharField(max_length=30)
    date = models.DateField()
    maxPlayers = models.IntegerField()
    participants = models.ManyToManyField(Player)
    pass
    
  
class Game(models.Model):
    tournament = models.ForeignKey(Tournament,on_delete=models.CASCADE)
    player1 = models.ForeignKey(Player,related_name='player1',on_delete=models.CASCADE)
    player2 = models.ForeignKey(Player,related_name='player2',on_delete=models.CASCADE)