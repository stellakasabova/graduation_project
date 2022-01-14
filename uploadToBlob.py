from zipFiles import zipFiles
from azure.storage.blob import BlobServiceClient
import os

def upload_blob(path):
    connection = open("connection_string.txt", "r")
    connection_string = connection.read()
    blob_container = "blob"

    zipFiles(path)
    file_name = 'test.zip'
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    blob_client = blob_service_client.get_blob_client(container=blob_container, blob=file_name)

    with open(os.path.join('D:\diplomna', 'test.zip'), "rb") as data:
        blob_client.upload_blob(data, overwrite=True)

    connection.close()
