# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from southdb.models import Song
from south.db import db


def get_song(request, song_id):
    #having issues with variable song_ids
    ids = db.Song.id #getting ids from id column
    for song_id in ids: #looping through ids
        if not song_id in d['song']: #if the specific song's info hasn't been put into a dictionary yet:
            song = Song.objects.get(song_id) #get the specific song's info
            d = {'song':song} #put the info in a dictionary
    return render_to_response('players/index.html', d) #from previous...
    
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
        #with POST data. This prevents data from being posted twice is a
        #user hits the Back button.
        #return HttpResponseRedirect(reverse('poll_results', args=(p.id,)))

#https://docs.djangoproject.com/en/dev/intro/tutorial04/#write-a-simple-form
