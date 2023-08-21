from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse

articles = {
    'sports': 'Sports Page',
    'finance':  'Finance Page',
    'politics':  'Politics Page',
}

# Create your views here.
def num_page_view(request, num_page):
    topics_list = list(articles.keys())
    topic = topics_list[num_page]

    webpage = reverse('topic-page', args=[topic])

    return HttpResponseRedirect(webpage)


def news_view(request, topic) -> HttpResponse:
    try:
        return HttpResponse(articles[topic])
    except:
        raise Http404("404 GENERIC ERROR") # this exception thrown here will be later caught by our project-wide error handler

def add_view(request, num1, num2) -> HttpResponse:
    result = num1 + num2
    return HttpResponse(str(result))