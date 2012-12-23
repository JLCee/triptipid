from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.ForeignKey(User, unique=True)
	picture_url = models.URLField()
	facebook_account = models.URLField()
	twitter_account = models.URLField()
	gplus_account = models.URLField()
	linkedin_account = models.URLField()
	wordpress_account = models.URLField()
	blogger_account = models.URLField()
	skype_account = models.URLField()
	pinterest_account = models.URLField()
	
	def __unicode__(self):
		return self.user.username
	
