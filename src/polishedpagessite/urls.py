from django.conf.urls import patterns, include, url
from django.contrib.auth.views import logout_then_login
from .views import HomeView, LoginView, RegisterView, RegistrationCompleteView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

# Page requests
urlpatterns = patterns('polishedpagessite.views',
    url(r'^$', HomeView.as_view(), name='home'),

    # Login/logout
    url(r'^account/login$', LoginView.as_view(), name='login'),
    url(r'^account/logout$', logout_then_login, name='logout'),

    # Account registration
    url(r'^account/register$', RegisterView.as_view(), name='register'),
    url(r'^account/registered$', RegistrationCompleteView.as_view(), name='registration_complete'),
)

# TODO: Add API routing when APIs are available
