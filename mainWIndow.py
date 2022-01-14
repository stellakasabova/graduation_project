from uploadToBlob import upload_blob
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

root = Tk()
root.title('Application')
root.geometry("150x150")

def directory():
    path = filedialog.askdirectory()
    upload_blob(path)
    messagebox.showinfo("Done", "Upload finished")

dir_button = Button(root, text="Archive directory", command=directory).place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()
