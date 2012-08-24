from django.shortcuts import render_to_response, get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from models import Song, Playlist, User
import random
from django.contrib.auth import authenticate, login, logout
from django.core.context_processors import csrf
from django.core import serializers
import re
from django.db.models import Q
import operator


def home_view(request):
    return render_to_response("home.html")

def list_songs(request):
    keywords = request.GET.get('keywords')
    #previous statement used to end in " .strip() "
    print keywords

    if request.user.is_authenticated():
        playlists = request.user.playlist_set.all()
    else:
        playlists = []
    song_query = Song.objects
    "select * from Song;"
    songs_query = song_query.order_by("-id")
    "select * from Song order by id desc;"
    
    if keywords:
        individual_words = keywords.split()
        q = Q() 	
        for word in individual_words:
            q = operator.or_(q, Q(name__icontains = word))	
            q = operator.or_(q, Q(artist__icontains = word))
            songs_query = songs_query.filter(q)
		
    songs = songs_query.all();

    json_songs = serializers.serialize("json", songs)
    return render(request, 'sample.html', { "json_songs": json_songs,
                                            "all_songs": songs,
                                            "all_playlists": playlists})

def playlist(request, playlist_id):
    playlist = Playlist.objects.get(id = playlist_id)
    if request.user.is_authenticated():
        playlists = request.user.playlist_set.all()
    else:
        playlists = []
    songs = playlist.songs.all()
    json_songs = serializers.serialize("json", songs)
    return render(request, 'sample.html', { "json_songs": json_songs,
                                            "all_songs": songs, 
					    "all_playlists": playlists})

def make_playlist(request):
    return render(request, 'sample.html')

#def create_playlist(request):
    #user = request.user.name
    #whoever is logged in is the user
    #name = request.POST.get(name)
    #need an input form for name
    #songs = request.POST.get(songs)
    #songs needs to equal the songs that they have chosen somehow
    #a list of song objects?
    #playlist = Playlist.objects.create(name=name, user=user, songs=songs)
    #return render(request, 'sample.html')

def go_search(request):
    return render(request, 'search.html')

#def search_keywords(songs, keywords):
    #if isinstance(keywords, str):
        #keywords=[keywords]
    #if not isinstance(keywords, list):
        #return None
    #list_songname_qs = [Q(name__icontains=x) for x in keywords]
    #list_artist_qs= [Q(artist__icontains=x) for x in keywords]
    #final_q = reduce(operator.or_, list_artist_qs + list_songname_qs)
    #r_qs = songs.filter(final_q)
    #return r_qs
    

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
