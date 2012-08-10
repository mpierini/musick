from django.db import models

import datetime 
from django.utils import timezone 

# Create your models here.
class Song(models.Model):
    #default primary_key is already an id field??
    url = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100, default="UNKNOWN")
    #why this no work???

    #blog_name = models.CharField(max_length=100) // link!
    #duration = models.IntegerField(null=False)
    #time_stamp = models.DateField()

    def __unicode__(self):
        return u"%s - %s"%(self.artist, self.name)

class Playlist(models.Model):
    songs = models.ManyToManyField(Song, related_name="+")
    name = models.CharField(max_length=64)
    #user_id?

    def __unicode__(self):
        return self.name

#class Users(models.Model);
    #username = models.CharField(max_length=100)
    #password = models.CharField(max_length=8) or weird salting and hashing thing?
    #playlists = models.ManyToManyField(Playlist)
    #they also have songs not in playlists, too? considered one unordered playlist?
    #account info/avatar pic maybe...
