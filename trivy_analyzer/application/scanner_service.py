import os
from pathlib import Path
import subprocess
from django.shortcuts import render

def clear_temp_folder():
    temp_uploads_path = Path('temp_uploads')
    files_in_folder = temp_uploads_path.iterdir()
    for file in files_in_folder:
        print(file)
        try:
            if file.is_file():
                file.unlink()
                print('Deleted file' + file)
            else:
                print('File ' + file + ' skipped')
        except Exception as e:
            print('Error deleting path ')


def search_uploaded_file():
    temp_uploads_path = Path('temp_uploads')
    files_in_folder = temp_uploads_path.iterdir()
    file_result = []
    for file in files_in_folder:
        file_result.append(file.as_posix())
    return file_result[0]

def scanner():
    file_to_scan = search_uploaded_file()
    process = subprocess.run('checkov -f ' + file_to_scan, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output = process.stdout
    clear_temp_folder() 
    if process.returncode == 0:
        print("Command executed successfully")
        print(output)   
    return output.split('\n')