""" Document/draft models. """
from django.db import models
from .authors import AuthorProfile

APP_LABEL = 'polishedpages'

class Document(models.Model):
    author = models.ForeignKey(AuthorProfile)
    class Meta:
        app_label = APP_LABEL

class Draft(models.Model):
    document = models.ForeignKey(Document)
    class Meta:
        app_label = APP_LABEL
