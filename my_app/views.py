from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse

articles = {
    'sports': 'Sports Page',
    'finance':  'Finance Page',
    'politics':  'Politics Page',
}

def simple_view(request):
    return render(request, 'my_app/example.html') # .html

def variable_view(request):
    my_var = { 'first_name': 'Hector', 'last_name': 'Serrano' }

    return render(request, 'my_app/variable.html', context=my_var)

# Create your views here.
def num_page_view(request, num_page):
    try:
        topics_list = list(articles.keys())
        topic = topics_list[num_page]

        if not topic:
            raise "page number doesn't exist"


        webpage = reverse('topic-page', args=[topic])

        return HttpResponseRedirect(webpage)
    except IndexError as indexError:
        raise Http404(f'out of bounds - {indexError}') # this exception thrown here will be later caught by our project-wide error handler



def news_view(request, topic) -> HttpResponse:
    try:
        return HttpResponse(articles[topic])
    except:
        raise Http404("404 GENERIC ERROR") # this exception thrown here will be later caught by our project-wide error handler

def add_view(request, num1, num2) -> HttpResponse:
    result = num1 + num2
    return HttpResponse(str(result))