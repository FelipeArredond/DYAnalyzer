import os
from pathlib import Path
import subprocess
from django.shortcuts import render
from analyzer.application.folders_managment_service import Folder_Manager

class Scanner_Service:
    def __init__(self, folder_manager) -> None:
        self.__folder_manager = folder_manager

    def scan(self):
        file_to_scan = self.__folder_manager.search_uploaded_file()
        process = subprocess.run('checkov -f ' + file_to_scan, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output = process.stdout 
        if process.returncode == 0:
            print("Command executed successfully")
            print(output)
        self.__folder_manager.clear_temp_folder()
        return output.split('\n') 