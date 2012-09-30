from django.contrib import admin
from models import Song, Playlist, UserProfile

#class SongInLine(admin.TabularInline):
    #model = Song
    #extra = 3
    
    #This tells Django: "Choice objects are edited on the Poll admin page.
    #By default, provide enough fields for 3 choices."


    #search_fields = ['question']
    #That adds a search box at the top of the change list. When somebody enters
    #search terms, Django will search the question field.

    #date_hierarchy = 'pub_date'
    #That adds hierarchical navigation, by date, to the top of the change list page.

admin.site.register(Song)
admin.site.register(Playlist)
admin.site.register(UserProfile)

#You'll follow this pattern -- create a model admin object,
#then pass it as the second argument to admin.site.register()
#-- any time you need to change the admin options for an object.
