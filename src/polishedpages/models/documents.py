""" Document/draft models. """
from django.db import models
from .authors import AuthorProfile

class Document(models.Model):
    author = models.ForeignKey(AuthorProfile)

class Draft(models.Model):
    document = models.ForeignKey(Document)
