from django.shortcuts import render
from django.http import HttpResponse, Http404

articles = {
    'sports': 'Sports Page',
    'finance':  'Finance Page',
    'politics':  'Politics Page',
}

# Create your views here.
def news_view(request, topic) -> HttpResponse:
    try:
        return HttpResponse(articles[topic])
    except:
        raise Http404("404 GENERIC ERROR") # this exception thrown here will be later caught by our project-wide error handler

def add_view(request, num1, num2) -> HttpResponse:
    result = num1 + num2
    return HttpResponse(str(result))
