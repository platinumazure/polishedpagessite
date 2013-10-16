""" User models. """
from django.db import models
from .authors import AuthorProfile

class UserProfile(models.Model):
    author_profile = models.ForeignKey(AuthorProfile)
