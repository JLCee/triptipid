from django import forms
from models import TransportationType, Itinerary, ItineraryRating, Day, ActivityType, Activity, CostType, Cost, KeyLocation, KeyLocationPhoto, RecentView, Badge, UserBadge

class TransportationTypeForm(forms.ModelForm):
	class Meta:
		model = TransportationType
		
class ItineraryForm(forms.ModelForm):
	class Meta:
		model = Itinerary

class ItineraryRatingForm(forms.ModelForm):
	class Meta:
		model = ItineraryRating

class DayForm(forms.ModelForm):
	class Meta:
		model = Day
		
class ActivityTypeForm(forms.ModelForm):
	class Meta:
		model = ActivityType
		
class ActivityForm(forms.ModelForm):
	class Meta:
		model = Activity

class CostTypeForm(forms.ModelForm):
	class Meta:
		model = CostType

class CostForm(forms.ModelForm):
	class Meta:
		model = Cost
		
class KeyLocationForm(forms.ModelForm):
	class Meta:
		model = KeyLocation
		
class KeyLocationPhotoForm(forms.ModelForm):
	class Meta:
		model = KeyLocationPhoto

class RecentViewForm(forms.ModelForm):
	class Meta:
		model = RecentView

class BadgeForm(forms.ModelForm):
	class Meta:
		model = Badge
		
class UserBadgeForm(forms.ModelForm):
	class Meta:
		model = UserBadge