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

    #url(r'^$', TemplateView.as_view(template_name="players/index.html")),
    url(r'^$', 'players.views.list_songs'),

    #url(r'^$',    
	#ListView.as_view(
            #queryset=Poll.objects.order_by('-pub_date')[:5],
            #context_object_name='latest_poll_list',
            #template_name='polls/index.html')),
    #url(r'^(?P<pk>\d+)/$',
        #DetailView.as_view(
            #model=Poll,
            #template_name='polls/detail.html')),
    #url(r'^(?P<pk>\d+)/results/$',
        #DetailView.as_view(
            #model=Poll,
            #template_name='polls/results.html'),
        #name='poll_results'),
    #url(r'^(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),
    #Using 2 generic views: ListView & DetailView. Respectively, those
    #2 views abstract the concepts of "display a list of objects" &
    #"display a detail page for a particular type of object."
)                       

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
urlpatterns += patterns('',
    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
)
