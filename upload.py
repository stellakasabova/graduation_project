import logging
from tkinter import *
import ftplib
import os
from tkinter import messagebox
from getImageData import addIPTCInfo

def upload(username_input, password_input, path, server_address):
    logging.basicConfig(level=logging.DEBUG, filename='logs.log', format='%(asctime)s %(levelname)s:%(message)s')
    logger = logging.getLogger(__name__)

    # Connect to FTP server
    session = ftplib.FTP(server_address)
    session.login(username_input.get(), password_input.get())

    if server_address == 'upload.alamy.com':
        session.cwd('/Stock')

    logger.info("Image upload started")
    try:
        # Gets images from directory
        img_extensions = ('.JPG', '.jpg', '.PNG', '.png')
        for file in os.listdir(path):
            if file.endswith(img_extensions):
                filename, ext = os.path.splitext(os.path.join(path, file))
                os.rename(os.path.join(path, file), filename+'.JPEG')

        for file in os.listdir(path):
            if file.endswith(('.JPEG', '.jpeg')):
                img_path = os.path.join(path, file)

                # Azure API only works with images 4MB and under
                if os.path.getsize(img_path) / (1024 * 1024) < 4:
                    addIPTCInfo(img_path)
                    session.storbinary('STOR ' + file, open(img_path, 'rb'))
                    print("upload "+img_path)
    except EOFError:
        logger.warning("Image upload failed")
    finally:
        logger.debug("Image upload done")

    # Upload IPTC data to FTP server
    logger.info("Metadata upload started")
    try:
        iptc_extensions = ('.JPEG~', '.jpeg~')
        for file in os.listdir(path):
            if file.endswith(iptc_extensions):
                iptc_path = os.path.join(path, file)
                session.storbinary('STOR ' + file, open(iptc_path, 'rb'))
                print("upload meta "+iptc_path)
    except EOFError:
        logger.warning("Metadata upload failed")
    finally:
        logger.debug("Metadata upload done")
        messagebox.showinfo("Done", "Upload done!")

    session.quit()

# Displays a pop-up window for logging in
def logInTopLevel(paths, server_address):
    login_window = Toplevel(height=300, width=300)
    if server_address == 'upload.alamy.com':
        username_label = Label(login_window, text="Email:")
        username_label.pack()
    else:
        username_label = Label(login_window, text="Username:")
        username_label.pack()
    username_input = Entry(login_window)
    username_input.pack()

    password_label = Label(login_window, text="Password: ")
    password_label.pack()
    password_input = Entry(login_window, show="*")
    password_input.pack()

    upload_func_button = Button(login_window, text="Upload", command=lambda: upload(username_input, password_input, paths, server_address))
    upload_func_button.pack()
