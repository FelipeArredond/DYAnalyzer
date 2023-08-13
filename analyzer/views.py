from django.shortcuts import render
from django.http import HttpResponse
import subprocess
import docker

client = docker.from_env()


# Create your views here.
def hello(request):
    return HttpResponse("Added Trivy to gh actions")

def hello2(request):
    return HttpResponse("Hello World2")

def trivy(request):
    
    # result = subprocess.run(['docker' , 'run', 'bitnami/trivy', 'image', 'python:3.4-alpine'], capture_output=True, text=True)
    result = subprocess.run(['ls'], capture_output=True, text=True)

    trivy_output = result.stdout
    print(trivy_output)
    return HttpResponse(trivy_output)

def docker(request):
    client.images.pull("bitnami/trivy")
    Container = client.containers.create('bitnami/trivy')
    Container.start()
    print(Container.status)
    Container.exec_run("")
    return HttpResponse("docker")