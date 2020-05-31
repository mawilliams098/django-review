from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Question


# request / response objects
"""
Django uses request and response objects to pass state through the system.

When a page is requested, Django creates an HttpRequest
object that contains metadata about the request. 
Then Django loads the appropriate view, passing the HttpRequest
as the first argument to the view function. 

Each view is responsible for returning an HttpResponse object.

Each view is responsible for doing one of two things: returning an HttpResponse object 
containing the content for the requested page, or raising an exception such as Http404. 
The rest is up to you.

1. load a template
2. fill a context
3. return an HttpResponse
"""

# to call the view, map it to a url in polls/urls.py
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context) # render returns an HttpResponse

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
    
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)