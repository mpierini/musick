from django.shortcuts import render_to_response, get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from models import Song, Playlist, User
import random
from django.contrib.auth import authenticate, login, logout
from django.core.context_processors import csrf
from django.core import serializers


def home_view(request):
    return render_to_response("home.html")

def list_songs(request):
    if request.user.is_authenticated():
        playlists = request.user.playlist_set.all()
    else:
        playlists = []
    songs = Song.objects.order_by('id').all();
    first_song = songs[0]

    json_songs = serializers.serialize("json", songs)
    #page_num = songs / 20
    #if songs % 20 != 0:
        #page_num += 1
    #print page_num
    return render(request, 'sample.html', { "json_songs": json_songs,
                                            "first_song": first_song,
                                            "all_playlists": playlists})

def playlist(request, playlist_id):
    playlist = Playlist.objects.get(id = playlist_id)
    if request.user.is_authenticated():
        playlists = request.user.playlist_set.all()
    else:
        playlists = []
    songs = playlist.songs.all()
    return render(request, 'sample.html', {"all_songs": songs, "all_playlists": playlists})
    

def user_login(request):
    username = request.POST.get("user")
    print username
    password = request.POST.get("password")
    print password
    user = authenticate(username=username, password=password)

    if user:
        print("Successfully logged in")
        login(request, user)
        return redirect("home")
    else:
        print "No such user"
        return render(request, "bad_login.html")

def user_logout(request):
    logout(request)
    return redirect("home")

def go_register(request):
    return render(request, "register.html")

def add_user(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    email = request.POST.get("email")
    url = request.POST.get("url")
    user = User.objects.create_user(username=username, password=password, email=email)
    p = user.get_profile()
    p.url = url
    user.save()
    p.save()

    user = authenticate(username=username, password=password)
    login(request, user)

    return redirect("home")

#def user_profile(request, user_id):
    #user = Users.objects.get(id = user_id)
    #return render_to_response('sample.html')

#Always return an HttpResponseRedirect after successfully dealing
#with POST data.

#https://docs.djangoproject.com/en/dev/intro/tutorial04/#write-a-simple-form
