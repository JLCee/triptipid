from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template import RequestContext

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required

from accounts.models import UserProfile
from django.contrib.auth.models import User
from models import TransportationType, Itinerary, ItineraryRating, Day, ActivityType, Activity, CostType, Cost, KeyLocation, KeyLocationPhoto, RecentView, Badge, UserBadge
from forms import TransportationTypeForm, ItineraryForm, ItineraryRatingForm, DayForm, ActivityTypeForm, ActivityForm, CostTypeForm, CostForm, KeyLocationForm, KeyLocationPhotoForm, RecentViewForm, BadgeForm, UserBadgeForm

import re
import simplejson as json

def home(request):
	return render_to_response('createitinerary.html', {}, context_instance=RequestContext(request))
	
@login_required
def user_account(request):
	profile = request.user.get_profile()
	
	if request.method == 'POST':
		if 'first_name' in request.POST and 'last_name' in request.POST:
			User.objects.filter(id__exact = profile.user_id).update(first_name=request.POST['first_name'], last_name=request.POST['last_name'])
		elif 'username' in request.POST:
			User.objects.filter(id__exact = profile.user_id).update(username=request.POST['username'])
		elif 'email' in request.POST:
			User.objects.filter(id__exact = profile.user_id).update(email=request.POST['email'])
		elif 'password' in request.POST:
			User.objects.filter(id__exact = profile.user_id).update(password=request.POST['password'])
		elif 'picture_url' in request.POST:
			User.objects.filter(id__exact = profile.user_id).update(picture_url=request.POST['picture_url'])

	profile = request.user.get_profile()
			
	return render_to_response('user.html', {
		'user_account': profile.user,
		'user_profile': profile,
		'statistics_itinerary': Itinerary.objects.filter(user_id__exact = profile.user_id).count(),
		'statistics_rating': 0,	
	}, context_instance=RequestContext(request))

@login_required
def view_itinerary(request):
	profile = request.user.get_profile()
	
	if request.method == "POST":
		if 'itinerary_id' in request.POST:
			itinerary = Itinerary.objects.get(id__exact=request.POST['itinerary_id'])

	return render_to_response('informative.html', {
		'selected_itinerary': profile.user,
	}, context_instance=RequestContext(request))

@login_required
def filter_itineraries(request):
	profile = request.user.get_profile()
	itineraries = set()
	
	if request.method == "POST":
		if 'location' in request.POST and 'destination' in request.POST and 'days' in request.POST:
			location = request.POST['location']
			destination = request.POST['destination']
			days = int(request.POST['days'])
			
			tempItineraries = Itinerary.objects.filter(location__icontains=request.POST['location'], destination__icontains=request.POST[destination])
			
			for obj in tempItineraries:
				nDays = Day.objects.filter(itinerary_id__exact = obj.id).count()
				if nDays == days:
					itineraries.add(obj)

	return render_to_response('itineraries.html', {
		'itinerary_list': itineraries,
	}, context_instance=RequestContext(request))

@login_required
def create_itinerary(request):
	profile = request.user.get_profile()
	
	if request.method == "POST":
		if 'location' in request.POST and 'destination' in request.POST and 'persons' in request.POST and 'transportation' in request.POST:
			itineraryForm = ItineraryForm({'starting_location': request.POST['location'], 'destination': request.POST['destination'], 'no_of_persons': int(request.POST['persons']), 'transportation_type': int(request.POST['transportation'])})
			itineraryForm.save()
			
			#Parse days JSON object
			objs = json.loads(request.POST['days'])

			#Iterate through days list
			for obj in objs:
				dayForm = DayForm(itinerary_id=obj.itinerary_id, day_number=obj.day_number)
				dayForm.save()
				
			#Parse activities JSON object
			objs = json.loads(request.POST['activities'])

			#Iterate through activities list
			for obj in objs:
				activityForm = ActivityForm(day_id=obj.day_id, activity_type_id=obj.activity_type_id, time_start=obj.time_start, description=obj.description, location_name=obj.location_name, address=obj.address, telephone_number=obj.telephone_number)
				activityForm.save()
				
			#Parse costs JSON object
			objs = json.loads(request.POST['costs'])

			#Iterate through costs list
			for obj in objs:
				costForm = CostForm(day_id=obj.day_id, cost_type_id=obj.cost_type_id, activity_name=obj.activity_name, activity_cost=obj.activity_cost)
				costForm.save()

			#Parse key_locations JSON object
			objs = json.loads(request.POST['key_locations'])

			#Iterate through key_locations list
			for obj in objs:
				keylocationForm = KeyLocationForm(itinerary_id=obj.itinerary_id, name=obj.name, description=obj.description, longitude=obj.longitude, latitude=obj.latitude)
				keylocationForm.save()	
			
			#Parse key_location_photos JSON object
			objs = json.loads(request.POST['key_location_photos'])

			#Iterate through key_location_photos list
			for obj in objs:
				keylocationphotosForm = KeyLocationPhotoForm(key_location_id=obj.key_location_id, photo_url=obj.photo_url)
				keylocationphotosForm.save()	
			
	return render_to_response('user.html', {
	}, context_instance=RequestContext(request))
	
