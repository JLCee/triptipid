from django.conf.urls import patterns, include, url

from views import *

urlpatterns = patterns('',
	url(r'^home/$', home, name='home'),
	url(r'^user_account/$', user_account, name='user_account'),
	url(r'^view_itinerary/$', view_itinerary, name='view_itinerary'),
	url(r'^filter_itineraries/$', filter_itineraries, name='filter_itineraries'),
	url(r'^create_itinerary/$', create_itinerary, name='create_itinerary'),
)
