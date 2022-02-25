from zipfile import ZipFile
import os
from os.path import basename

def zipFiles(path):
    extensions = ('.JPG', '.jpg', '.JPEG', '.jpeg', '.PNG', '.png')

    with ZipFile(path+'/archive.zip', 'w') as zip_object:
        for file in os.listdir(path):
            if file.endswith(extensions):
                file_path = os.path.join(path, file)
                zip_object.write(file_path, basename(file_path))
    zip_object.close()
