""" Views for rendering site pages. """
from django.core import urlresolvers
from django.views.generic import TemplateView, CreateView
from polishedpages.models import BasicUser
from polishedpages.forms import RegistrationForm

class HomeView(TemplateView):
    template_name = 'index.html'

class RegisterView(CreateView):
    model = BasicUser
    form_class = RegistrationForm
    template_name = 'register.html'
    success_url = urlresolvers.reverse_lazy('registration_complete')

class RegistrationCompleteView(TemplateView):
    template_name = 'registration_complete.html'
