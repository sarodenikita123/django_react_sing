from django.db import models

class Song(models.Model):
    name = models.CharField(max_length=20)
    sname = models.CharField(max_length=20)
    number = models.IntegerField()
