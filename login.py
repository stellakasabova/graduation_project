from tkinter import *
import ftplib
import os

def logIn(username_input, password_input, path):
    address = 'A32900B79A49CDDDE121D03A004BB565B.asuscomm.com'
    session = ftplib.FTP(address)
    session.login(username_input.get(), password_input.get())
    session.cwd('LINKSYS/stella')

    extensions = ('.JPG', '.jpg', '.JPEG', '.jpeg', '.PNG', '.png')
    for file in os.listdir(path):
        if file.endswith(extensions):
            img_path = os.path.join(path, file)
            session.storbinary('STOR ' + file, open(img_path, 'rb'))

    session.quit()
    print("success")

def uploadTopLevel(paths):
    upload_window = Toplevel(height=300, width=300)
    username_label = Label(upload_window, text="Username:")
    username_label.pack()
    username_input = Entry(upload_window)
    username_input.pack()

    password_label = Label(upload_window, text="Password: ")
    password_label.pack()
    password_input = Entry(upload_window, show="*")
    password_input.pack()

    upload_func_button = Button(upload_window, text="Upload", command=lambda: logIn(username_input, password_input, paths))
    upload_func_button.pack()

