from django.conf.urls import patterns, include, url
from .views import HomeView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

# Page requests
urlpatterns = patterns('polishedpagessite.views',
    url(r'^$', HomeView.as_view(), name='home'),
)

# TODO: Add API routing when APIs are available
