#from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    #return HttpResponse("Hello there!")
    return render(request, "home.html") #it means that we request and render the "home.html" template

def about(request):
    #return HttpResponse("My About page")
    return render(request, "about.html")