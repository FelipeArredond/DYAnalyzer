from django.shortcuts import render
from django.http import HttpResponse, request
from .application.scanner_service import scanner

def scanner_view(request):
    response = scanner()
    print(response[0])
    print(response[1])
    print(response[2])
    print(response[3])


    tittle = 'Test Results'
    return render(request, 'results.html', {
        'tittle': tittle,
        'items': response
    })
