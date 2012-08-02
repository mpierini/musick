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
    #songs = models.ManyToManyField(Song)

#did initial migration with class Song fields: id / url / name
