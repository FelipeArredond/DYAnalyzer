from django.shortcuts import render
from django.http import HttpResponse
import subprocess
import docker

client = docker.from_env()


# Create your views here.
def hello(request):
    return HttpResponse("Added Trivy to gh actions")