from django.shortcuts import render

""" Views for rendering site pages. """

def home(request):
    return render(request, 'index.html')

def demo(request):
    return render(request, 'review_engine_demo.html')
