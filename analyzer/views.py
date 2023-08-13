from django.shortcuts import render
from django.http import HttpResponse
from .application.analyze import downloadTrivyImage

def hello(request):
    result = downloadTrivyImage()
    return HttpResponse(result)

def about(request):
    # downloadTrivyImage()
    return HttpResponse("About")