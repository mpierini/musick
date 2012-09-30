from django.db import models
import datetime 
from django.utils import timezone 
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Song(models.Model):
    url = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100, default="UNKNOWN")

    #blog_name = models.CharField(max_length=100) // link!
    #duration = models.IntegerField(null=False)
    #time_stamp = models.DateField()

    def __unicode__(self):
        return u"%s - %s"%(self.artist, self.name)

class Playlist(models.Model):
    songs = models.ManyToManyField(Song, related_name="+")
    name = models.CharField(max_length=64)
    user = models.ForeignKey(User)
    #something might be wrong with the migration of this

    def __unicode__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    url = models.CharField(max_length = 100, blank = True)
    #avatar = models.ImageField(upload_to="/static/", default="/static/face.png")
    #this is not migrating but it may be because of the playlist_user entry

    #playlists = models.ManyToManyField(Playlist)
    #they also have songs not in playlists, too? considered one unordered playlist?

    def __unicode__(self):
        return self.user.email


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
