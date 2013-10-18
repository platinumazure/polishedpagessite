""" Author models. """
from django.db import models
from .users import BasicUser

APP_LABEL = 'polishedpages'

class AuthorProfile(models.Model):
    user = models.ForeignKey(BasicUser)

    class Meta:
        app_label = APP_LABEL
