import os
import PIL
from PIL import ImageTk, Image
from tkinter import *
from tkinter import filedialog

root = Tk()
root.title('Application')
root.geometry("1500x1500")
image_paths = []
images = []

def aa(path_param):
    global image_paths
    global images
    global image_label
    global button_back
    global button_forward

    extensions = ('.JPG', '.jpg', '.JPEG', '.jpeg', '.PNG', '.png')
    for (root_, dirs, files) in os.walk(path_param):
        for file_ in files:
            if file_.endswith(extensions):
                path = os.path.join(path_param, file_)
                image_paths.append(path)

    for image in image_paths:
        temp = PIL.Image.open(image)
        temp = temp.resize((500, 500), PIL.Image.ANTIALIAS)
        temp_resized = ImageTk.PhotoImage(temp)
        images.append(temp_resized)

    image_label = Label(root, image=images[0])
    image_label.grid(row=0, column=0, columnspan=3)

    button_back = Button(root, text="<<", command=back, state=DISABLED).grid(row=1, column=0)
    button_forward = Button(root, text=">>", command=lambda: forward(2)).grid(row=1, column=2)

    dir_button.grid_forget()

def forward(image_number):
    global image_label
    global button_back
    global button_forward

    image_label.grid_forget()
    image_label = Label(image=images[image_number - 1])

    button_back = Button(root, text="<<", command=lambda: back(image_number-1))
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))

    if image_number == len(images):
        button_forward = Button(root, text=">>", state=DISABLED)

    image_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

def back(image_number):
    global image_label
    global button_back
    global button_forward

    image_label.grid_forget()
    image_label = Label(image=images[image_number - 1])

    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))

    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    image_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

dir_button = Button(root, text="Choose directory", command=lambda: aa(filedialog.askdirectory()))
dir_button.grid(row=0, column=0)

image_label = ""
button_forward = ""
button_back = ""

root.mainloop()
