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

    blob_container = "blob"

    zipFiles(path, zip_name)
    file_name = zip_name+'.zip'
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    blob_client = blob_service_client.get_blob_client(container=blob_container, blob=file_name)

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

    messagebox.showinfo("Done", "Archiving done!")

