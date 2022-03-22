import json
import logging
import os

from azure.core.exceptions import HttpResponseError

from encrypt import *
from zipFiles import zipFiles
from azure.storage.blob import BlobServiceClient
from tkinter import messagebox

def uploadBlob(path, zip_name):
    decrypted_data = str(decryptKeys())
    decrypted_data.replace("'", '"')

    result = json.loads(decrypted_data)
    connection_string = result["connection"]

    with open('sas_keys.json', 'w') as file:
        file.write(decrypted_data)
        file.close()

    encryptKeys()

    zipFiles(path, zip_name)
    file_name = zip_name+'.zip'

    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    blob_client = blob_service_client.get_blob_client(container="store", blob=file_name)

    logging.basicConfig(level=logging.DEBUG, filename='logs.log', format='%(asctime)s %(levelname)s:%(message)s')
    logger = logging.getLogger(__name__)

    logger.info("Attempting archiving")

    try:
        with open(os.path.join(path, file_name), "rb") as data:
            blob_client.upload_blob(data, overwrite=True)
    except HttpResponseError:
        logger.warning("Archiving failed")
    finally:
        logger.debug("Archiving done")

    os.remove(path + "/" + file_name)
    messagebox.showinfo("Done", "Archiving done!")

def downloadBlob(path, zip_name):
    decrypted_data = str(decryptKeys())
    decrypted_data.replace("'", '"')

    result = json.loads(decrypted_data)
    connection_string = result["connection"]

    with open('sas_keys.json', 'w') as file:
        file.write(decrypted_data)
        file.close()

    encryptKeys()

    blob_name = zip_name+'.zip'
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    container = blob_service_client.get_container_client("store")

    logging.basicConfig(level=logging.DEBUG, filename='logs.log', format='%(asctime)s %(levelname)s:%(message)s')
    logger = logging.getLogger(__name__)

    logger.info("Attempting download")

    try:
        with open(os.path.join(path, blob_name), "wb") as file:
            file.write(container.get_blob_client(blob_name).download_blob().readall())
    except HttpResponseError:
        logger.warning("Download failed")
    finally:
        logger.debug("Download done")

    messagebox.showinfo("Done", "Download done!")
