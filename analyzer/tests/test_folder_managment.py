from django.test import TestCase
import subprocess
from pathlib import Path

from analyzer.application.folders_managment_service import Folder_Manager


class TestFolderManagment(TestCase):

    def test_clear_temp_folder(self):
        folder_manager = Folder_Manager()
        creting_file_process = subprocess.run('cd temp_uploads && touch test.txt', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        folder_manager.clear_temp_folder()
        verify_folder = subprocess.run('ls temp_uploads', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        result = verify_folder.stdout
        self.assertEquals(result, '')

    def test_search_uploaded_file(self):
        folder_manager = Folder_Manager()
        creting_file_process = subprocess.run('cd temp_uploads && touch test.txt', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        self.assertEquals(folder_manager.search_uploaded_file(), 'temp_uploads/test.txt')