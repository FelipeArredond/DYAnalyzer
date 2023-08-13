from django.shortcuts import render
from django.http import HttpResponse, request
from django.shortcuts import render

def index(request):
    tittle = 'Django DockerFiles Analyzer'
    return render(request, 'index.html', {
        'tittle': tittle
    })
