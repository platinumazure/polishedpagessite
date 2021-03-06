""" User models. """
from django.db import models
from django.dispatch import receiver
from django.utils.translation import ugettext as _
from django.contrib import messages
from django.contrib.auth.signals import user_logged_out
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

APP_LABEL = 'polishedpages'

class BasicUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        "Creates and saves a user with the given email and password."
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        "Creates and saves a superuser with the given email and password."
        user = self.create_user(email, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user

class BasicUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        db_index=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = BasicUserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        app_label = APP_LABEL

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __unicode__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have specific permissions?"
        # Simplest possible answer: Yes
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

# Signal handlers
@receiver(user_logged_out, sender=BasicUser)
def add_logout_message(sender, request, **kwargs):
    messages.success(
        request,
        _('You have successfully logged out. Thank you for using '
            'Polished Pages!'),
        fail_silently=True,
    )
