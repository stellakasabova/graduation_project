import logging

from azure.core.exceptions import HttpResponseError

from zipFiles import zipFiles
from azure.storage.blob import BlobServiceClient
import os
from tkinter import messagebox

def upload_blob(path):
    connection = open("connection_string.txt", "r")
    connection_string = connection.read()
    blob_container = "blob"

    zipFiles(path)
    file_name = 'archive.zip'
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    blob_client = blob_service_client.get_blob_client(container=blob_container, blob=file_name)

    logging.basicConfig(level=logging.DEBUG, filename='logs.log', format='%(asctime)s %(levelname)s:%(message)s')
    logger = logging.getLogger(__name__)

    logger.info("Attempting archiving")
    try:
        with open(os.path.join(path, 'archive.zip'), "rb") as data:
            blob_client.upload_blob(data, overwrite=True)
    except HttpResponseError:
        logger.warning("Archiving failed")
    finally:
        logger.debug("Archiving done")

    connection.close()
    messagebox.showinfo("Done", "Archiving done!")

