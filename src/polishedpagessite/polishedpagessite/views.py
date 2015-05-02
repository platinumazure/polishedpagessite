""" Views for rendering site pages. """
from django.core import urlresolvers
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.views import generic
from polishedpages.models import BasicUser
from polishedpages.forms import RegistrationForm

class HomeView(generic.TemplateView):
    template_name = 'index.html'

class LoginView(generic.FormView):
    model = BasicUser
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = urlresolvers.reverse_lazy('home')

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)

class RegisterView(generic.CreateView):
    model = BasicUser
    form_class = RegistrationForm
    template_name = 'register.html'
    success_url = urlresolvers.reverse_lazy('registration_complete')

class RegistrationCompleteView(generic.TemplateView):
    template_name = 'registration_complete.html'
