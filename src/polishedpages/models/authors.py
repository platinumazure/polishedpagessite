""" Author models. """
from django.db import models

APP_LABEL = 'polishedpages'

class AuthorProfile(models.Model):
    class Meta:
        app_label = APP_LABEL
