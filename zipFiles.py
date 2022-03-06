import os
from os.path import basename
from zipfile import ZipFile

def zipFiles(path, name):
    extensions = ('.JPG', '.jpg', '.JPEG', '.jpeg', '.PNG', '.png')

    with ZipFile(path+'/'+name+'.zip', 'w') as zip_object:
        for file in os.listdir(path):
            if file.endswith(extensions):
                file_path = os.path.join(path, file)
                zip_object.write(file_path, basename(file_path))
    zip_object.close()
