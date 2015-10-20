from django.db import models

class Quest(models.Model):
    name = models.CharField(max_length=40)

class Station(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    time = models.IntegerField()
    location = models.CharField(max_length=50)
# Create your models here.
