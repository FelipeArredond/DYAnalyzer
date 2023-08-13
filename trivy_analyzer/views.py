from django.shortcuts import render
from django.http import HttpResponse, request
from .application.scanner_service import scanner

def scanner_view(request):
    response = scanner()
    items_to_render = []
    i = 0
    # while i < 8:
    #     print(response[i])
    #     i+=1
    while i < len(response):
        if(i>8):
            items_to_render.append(response[i])
        i+=1

    tittle = 'Test Results'
    return render(request, 'results.html', {
        'tittle': tittle,
        'items': items_to_render
    })
