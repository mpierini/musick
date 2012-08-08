from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'players.views.home_view', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),
    url(r'^players/', include('players.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r"^playlist/(?P<playlist_id>\d+)/$", "players.views.playlist", name="playlist"),
)



   # url(r'^polls/(?P<poll_id>\d+)/$', 'polls.views.detail'),
