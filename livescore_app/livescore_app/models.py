from django.db import models
from django.urls import reverse

# Create your models here.

class Player(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    dateOfBirth = models.DateField()
    nickname = models.CharField(max_length=12,unique=True)  #every nickname must be unique for user identification
    email = models.EmailField()
    
    
    def get_absolute_url(self):
        return reverse("player-detail", kwargs={"my_id" : self.id})

class Tournament(models.Model):
    name= models.CharField(max_length=30)
    venue = models.CharField(max_length=30)
    date = models.DateField()
    maxPlayers = models.IntegerField()
  