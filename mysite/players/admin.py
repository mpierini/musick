from django.contrib import admin
from models import Song, Playlist, UserProfile

#class SongInLine(admin.TabularInline):
    #model = Song
    #extra = 3
    
    #This tells Django: "Choice objects are edited on the Poll admin page.
    #By default, provide enough fields for 3 choices."

#class PollAdmin(admin.ModelAdmin):
   # fieldsets = [
       #(None,               {'fields' : ['question']}),
       #('Date information', {'fields' : ['pub_date'], 'classes' : ['collapse']}),
   # ] #The first element of each tuple in fieldsets is the title of the fieldset.
      #You can assign arbitrary HTML classes to each fieldset. Django provides
      #a "collapse" class that displays a particular fieldset initially collapsed.
    
   #inlines = [ChoiceInline]
    
    #list_display = ('question', 'pub_date', 'was_published_recently')    
    #use the list_display admin option, which is a tuple of field names
    #to display, as columns, on the change list page for the object:

    #list_filter = ['pub_date']
    #That adds a "Filter" sidebar that lets people filter the change list by the
    #pub_date field:

    #search_fields = ['question']
    #That adds a search box at the top of the change list. When somebody enters
    #search terms, Django will search the question field.

    #date_hierarchy = 'pub_date'
    #That adds hierarchical navigation, by date, to the top of the change list page.

admin.site.register(Song)
admin.site.register(Playlist)
admin.site.register(UserProfile)


#admin.site.register(Poll, PollAdmin)
#You'll follow this pattern -- create a model admin object,
#then pass it as the second argument to admin.site.register()
#-- any time you need to change the admin options for an object.

#admin.site.register(Choice)
