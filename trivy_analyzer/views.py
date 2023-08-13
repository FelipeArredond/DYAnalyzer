from django.shortcuts import render
from django.http import HttpResponse, request
from .application.scanner_service import scanner

def scanner_view(request):
    response = scanner()
    return HttpResponse(response)
