from django.shortcuts import render
from django.http import HttpResponse, request
from analyzer.application.folders_managment_service import Folder_Manager
from .application.scanner_service import Scanner_Service
from .application.form import FileUploadForm
import os

def scanner_view(request):
    folder_manager = Folder_Manager()
    scanner = Scanner_Service(folder_manager)
    response = scanner.scan()
    items_to_render = []
    i = 0
    while i < len(response):
        if(i>10):
            items_to_render.append(str(response[i]).upper().split(' '))
        i+=1

    tittle = 'Test Results'
    return render(request, 'results.html', {
        'tittle': tittle,
        'items': items_to_render
    })

def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.cleaned_data['file']
            temp_folder = 'temp_uploads/'
            os.makedirs(temp_folder, exist_ok=True)
            file_path = os.path.join(temp_folder, uploaded_file.name)
            with open(file_path, 'wb') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)
            return render(request, 'upload_success.html')
    else:
        form = FileUploadForm()
    return render(request, 'upload_form.html', {'form': form})