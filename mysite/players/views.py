# Create your views here
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from models import Song, Playlist

def home_view(request):
    return render_to_response("home.html")

def list_songs(request):
    songs = Song.objects.all().order_by('-id')
    return render_to_response('sample.html', {"all_songs": songs})

def list_playlists(request):
    playlists = Playlist.objects.all()
    return render_to_response('sample.html', {"all_playlists": playlists})
    #i don't get how to fix this, but i tried to make a new view dedicated to
    #listing the playlists


def playlist(request, playlist_id):
    playlist = Playlist.objects.get(id = playlist_id)
    playlists = Playlist.objects.all()
    songs = playlist.songs.all()
    return render_to_response('sample.html', {"all_songs": songs, "all_playlists": playlists})
    #playlist info appears on playlist/1/ page but not on sample.html

  
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
