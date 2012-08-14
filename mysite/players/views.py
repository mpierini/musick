# Create your views here
from django.shortcuts import render_to_response, get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from models import Song, Playlist, User
import random
from django.contrib.auth import authenticate, login, logout


def home_view(request):
    return render_to_response("home.html")

def list_songs(request):
    if request.user.is_authenticated():
        playlists = request.user.playlist_set.all()
    else:
        playlists = []

    songs = Song.objects.all().order_by('-id')
    return render(request, 'sample.html', {"all_songs": songs,
        "all_playlists": playlists})

def playlist(request, playlist_id):
    playlist = Playlist.objects.get(id = playlist_id)
    if request.user.is_authenticated():
        playlists = request.user.playlist_set.all()
    else:
        playlists = []
    songs = playlist.songs.all()
    return render(request, 'sample.html', {"all_songs": songs, "all_playlists": playlists})
    #playlist info appears on playlist/playlist_id/ page but not on sample.html

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


#def user_profile(request, user_id):
    #user = Users.objects.get(id = user_id)
    #return render_to_response('sample.html')

  
    #for song_id in ids: #looping through ids
        #if not song_id in d['song']: #if the specific song's info hasn't been put into a dictionary yet:
            #song = Song.objects.get(song_id) #get the specific song's info
            #d = {'song':song} #put the info in a dictionary
    #return render_to_response('sample.html') #, d) from previous...
    
    #p = get_object_or_404(Song, pk=song_id)
    #try:
        #selected_choice = p.choice_set.get(pk=request.POST['choice'])
    #except (KeyError, Choice.DoesNotExist):
        #Redisplay the poll voting form.
        #return render_to_response('polls/detail.html', {
            #'poll' : p,
            #'error_message' : "You didn't select a choice.",
            #}, context_instance=RequestContext(request))
    #else:
        #selected_choice.votes += 1
        #selected_choice.save()
        #Always return an HttpResponseRedirect after successfully dealing
        #with POST data.

#https://docs.djangoproject.com/en/dev/intro/tutorial04/#write-a-simple-form
