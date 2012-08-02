from django.db import models

# Create your models here.
class Song(models.Model):
    id = models.IntegerField(primary_key=True)
    #default primary_key is already an id field??
    url = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    #blog_name = models.CharField(max_length=100) // link!
    #duration = models.IntegerField(null=False)
    #time_stamp = models.DateField()

#class Playlist(models.Model):
    #id = models.IntegerField(primary_key=True) keep it default, tho?
    #songs = models.ManyToManyField(Song)

#class Users(models.Model);
    #id = models.IntegerField(primary_key=True) default?
    #username = models.CharField(max_length=100)
    #password = models.CharField(max_length=8) or weird salting and hashing thing?
    #playlists = models.ManyToManyField(Playlist)
    #they also have songs not in playlists, too? considered one unordered playlist?
    #account info/avatar pic maybe...
