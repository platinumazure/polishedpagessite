""" User models. """
from django.db import models
from .authors import AuthorProfile

APP_LABEL = 'polishedpages'

class UserProfile(models.Model):
    author_profile = models.ForeignKey(AuthorProfile)
    class Meta:
        app_label = APP_LABEL
