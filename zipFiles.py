from zipfile import ZipFile
import os
from os.path import basename


def zipFiles(path):
    with ZipFile('test.zip', 'w') as zip_object:
        for folder_name, sub_folders, files in os.walk(path):
            for filename in files:
                file_path = os.path.join(folder_name, filename)
                zip_object.write(file_path, basename(file_path))
    zip_object.close()
