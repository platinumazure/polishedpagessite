from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

# Page requests
urlpatterns = patterns('polishedpagessite.views',
    url(r'^$', 'home', name='home'),
)

# TODO: Add API routing when APIs are available
