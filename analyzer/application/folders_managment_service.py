import os
from pathlib import Path

class Folder_Manager:
    def __init__(self) -> None:
        print("Folder Manager Instanstiated")
    
    @staticmethod
    def clear_temp_folder() -> None:
        temp_uploads_path = Path('temp_uploads')
        files_in_folder = temp_uploads_path.iterdir()
        for file in files_in_folder:
            try:
                if file.is_file():
                    file.unlink()
                    print('Deleted file' + file)
                else:
                    print('File ' + file + ' skipped')
            except Exception as e:
                print('Error deleting path ')

    @staticmethod
    def search_uploaded_file() -> []:
        temp_uploads_path = Path('temp_uploads')
        files_in_folder = temp_uploads_path.iterdir()
        file_result = []
        for file in files_in_folder:
            file_result.append(file.as_posix())
        return file_result[0]