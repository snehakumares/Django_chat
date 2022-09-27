from re import M
from django.db import models
from datetime import datetime

class Room(models.Model):
    name = models.CharField(max_length=1000)

class Message(models.Model):
    roomid = models.IntegerField()
    username = models.CharField(max_length=1000)
    value = models.CharField(max_length=100000)
    time = models.DateTimeField(default=datetime.now, blank=True)
    
    