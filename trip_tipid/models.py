from django.db import models
from accounts.models import UserProfile

class TransportationType(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	
	def __unicode__(self):
		return self.name

class Itinerary(models.Model):
	user = models.ForeignKey(UserProfile)
	name = models.CharField(max_length=100)
	transportation_type = models.ForeignKey('TransportationType')
	starting_location = models.CharField(max_length=100)
	destination = models.CharField(max_length=100)
	no_of_persons = models.IntegerField()
	
	def __unicode__(self):
		return self.name

class ItineraryRating(models.Model):
	user = models.ForeignKey(UserProfile)
	itinerary = models.ForeignKey('Itinerary')
	rating = models.IntegerField()
	timestamp = models.DateTimeField(auto_now_add=True)
	
	def __unicode__(self):
		return self.rating
	
class Day(models.Model):
	itinerary = models.ForeignKey('Itinerary')
	day_number = models.IntegerField()
	
	def __unicode__(self):
		return self.number

class ActivityType(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	
	def __unicode__(self):
		return self.name
	
class Activity(models.Model):
	day = models.ForeignKey('Day')
	activity_type = models.ForeignKey('ActivityType')
	time_start = models.TimeField()
	description = models.TextField()
	location_name = models.CharField(max_length=100)
	address = models.CharField(max_length=200)
	telephone_number = models.CharField(max_length=100)
	
	def __unicode__(self):
		return self.location_name

class CostType(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	
	def __unicode__(self):
		return self.name
	
class Cost(models.Model):
	day = models.ForeignKey('Day')
	cost_type = models.ForeignKey('CostType')
	activity_name = models.CharField(max_length=100)
	activity_cost = models.FloatField()
	
	def __unicode__(self):
		return self.activity_name

class KeyLocation(models.Model):
	itinerary = models.ForeignKey('Itinerary')
	name = models.CharField(max_length=100)
	description = models.TextField()
	longitude = models.FloatField()
	latitude = models.FloatField()
	
	def __unicode__(self):
		return self.name
	
class KeyLocationPhoto(models.Model):
	key_location = models.ForeignKey('KeyLocation')
	photo_url = models.URLField()
	
	def __unicode__(self):
		return self.photo_url
	
class RecentView(models.Model):
	user = models.ForeignKey(UserProfile)
	itinerary = models.ForeignKey('Itinerary')
	timestamp = models.DateTimeField(auto_now_add=True)
	
	def __unicode__(self):
		return self.itinerary

class Badge(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	image_url = models.URLField()
	
	def __unicode__(self):
		return self.name
	
class UserBadge(models.Model):
	user = models.ForeignKey(UserProfile)
	badge = models.ForeignKey('Badge')
	
	def __unicode__(self):
		return self.badge

	