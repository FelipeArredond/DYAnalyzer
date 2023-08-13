from django.shortcuts import render
from django.http import HttpResponse
from .application.analyze_service import downloadTrivyImage

# Create your views here.
def hello(request):
    result = downloadTrivyImage()
    return HttpResponse(result)
