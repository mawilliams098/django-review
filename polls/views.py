from django.shortcuts import render

from django.http import HttpResponse

# request / response objects
"""
Django uses request and response objects to pass state through the system.

When a page is requested, Django creates an HttpRequest
object that contains metadata about the request. 
Then Django loads the appropriate view, passing the HttpRequest
as the first argument to the view function. 

Each view is responsible for returning an HttpResponse object.
"""

# to call the view, map it to a url in polls/urls.py
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")