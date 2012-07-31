from django.db import models

# Create your models here.
class Song(models.Model):
    id = models.IntegerField(null=False)
    #default primary_key is already an id field??
    url = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    #artist = models.CharField(max_length=100)
    #blog_name = models.CharField(max_length=100)
    #duration = models.IntegerField(null=False)
    #time_stamp = models.DateField()

#class Playlist(models.Model):
    #songs = models.ManyToManyField(Song)
