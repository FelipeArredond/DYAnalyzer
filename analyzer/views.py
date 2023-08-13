from django.shortcuts import render
from django.http import HttpResponse
from .application.analyze_service import downloadTrivyImage

def hello(request):
    return HttpResponse("<h1>Vulnerabilities Scanner</h1>")

def scan(request):
    result = downloadTrivyImage()
    return HttpResponse(result)
