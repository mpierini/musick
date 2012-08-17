from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView, TemplateView
from models import Song

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),
    
    url(r'^$', 'players.views.list_songs'),    
    url(r'^$', 'players.views.go_register'),
)                       

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
urlpatterns += patterns('',
    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
)
