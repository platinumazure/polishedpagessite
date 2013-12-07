""" Author models. """
from django.db import models
from django.utils.translation import ugettext_lazy as _
from .users import BasicUser

APP_LABEL = 'polishedpages'

class AuthorProfile(models.Model):
    user = models.ForeignKey(BasicUser)

    public_name = models.CharField(
        max_length=100,
        db_index=True,
        verbose_name=_('pen name'),
    )

    about = models.CharField(
        max_length=140,
        blank=True,
        verbose_name=_('summary'),
    )

    verbose_about = models.TextField(
        blank=True,
        verbose_name=_('about the author'),
    )

    favorite_authors = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='favorite_authors+',
    )

    class Meta:
        app_label = APP_LABEL
        verbose_name = _('author')
        verbose_name_plural = _('authors')
