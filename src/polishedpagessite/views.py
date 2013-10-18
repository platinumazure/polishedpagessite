""" Views for rendering site pages. """
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'index.html'
