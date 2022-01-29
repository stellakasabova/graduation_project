import os
import PIL
from PIL import ImageTk, Image
from tkinter import *
from tkinter import filedialog
from getTags import getTags
from uploadToBlob import upload_blob

root = Tk()
root.title('Application')
root.geometry("800x800")
image_paths = []
images = []
tag_arr = []

image_frame = ""
tag_frame = ""

def getImageTags(path):
    global tag_frame

    arr = getTags(path)
    tags = []
    for i in range(0, len(arr)):
        empty_label = Label(tag_frame, text="")
        tags.append(empty_label)

    for j in range(0, len(tags)):
        tags[j].configure(text=arr[j].name)

    return tags

def getImages(path_param):
    global image_paths
    global images
    global image_label
    global button_back
    global button_forward
    global tag_arr
    global image_frame
    global tag_frame
    global archive_button

    extensions = ('.JPG', '.jpg', '.JPEG', '.jpeg', '.PNG', '.png')
    for file in os.listdir(path_param):
        if file.endswith(extensions):
            path = os.path.join(path_param, file)
            if os.path.getsize(path) / (1024 * 1024) < 4:
                image_paths.append(path)

    for image in image_paths:
        temp_image = PIL.Image.open(image)
        temp_image = temp_image.resize((500, 500), PIL.Image.ANTIALIAS)
        temp_resized = ImageTk.PhotoImage(temp_image)
        images.append(temp_resized)

    image_frame = Frame(root, width=700, height=700)
    image_frame.place(anchor=CENTER, relx=.4, rely=.5)
    tag_frame = Frame(root)
    tag_frame.place(anchor=CENTER, relx=.65, rely=.5)

    tag_arr = getImageTags(image_paths[0])
    for g in range(0, len(tag_arr)):
        tag_arr[g].grid(row=g, column=0)

    image_label = Label(image_frame, image=images[0])
    image_label.grid(row=0, column=0, columnspan=3)

    button_back = Button(image_frame, text="<<", command=back, state=DISABLED).grid(row=1, column=0)
    button_forward = Button(image_frame, text=">>", command=lambda: forward(2)).grid(row=1, column=2)

    archive_button = Button(tag_frame, text="Archive directory", command=lambda: upload_blob(path_param)).grid(row=15)

    dir_button.destroy()

def forward(image_number):
    global image_label
    global button_back
    global button_forward
    global tag_arr

    for h in range(0, len(tag_arr)):
        tag_arr[h].grid_forget()

    image_label.grid_forget()
    image_label = Label(image_frame, image=images[image_number - 1])

    tag_arr = getImageTags(image_paths[image_number - 1])
    for k in range(0, len(tag_arr)):
        tag_arr[k].grid(row=k, column=0)

    button_back = Button(image_frame, text="<<", command=lambda: back(image_number-1))
    button_forward = Button(image_frame, text=">>", command=lambda: forward(image_number+1))

    if image_number == len(images):
        button_forward = Button(image_frame, text=">>", state=DISABLED)

    image_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

def back(image_number):
    global image_label
    global button_back
    global button_forward
    global tag_arr

    for u in range(0, len(tag_arr)):
        tag_arr[u].grid_forget()

    image_label.grid_forget()
    image_label = Label(image_frame, image=images[image_number - 1])

    tag_arr = getImageTags(image_paths[image_number - 1])
    for e in range(0, len(tag_arr)):
        tag_arr[e].grid(row=e, column=0)

    button_back = Button(image_frame, text="<<", command=lambda: back(image_number - 1))
    button_forward = Button(image_frame, text=">>", command=lambda: forward(image_number + 1))

    if image_number == 1:
        button_back = Button(image_frame, text="<<", state=DISABLED)

    image_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

dir_button = Button(root, text="Choose directory", command=lambda: getImages(filedialog.askdirectory()))
dir_button.place(anchor=CENTER, relx=.5, rely=.5)

image_label = ""
button_forward = ""
button_back = ""
archive_button = ""

root.mainloop()
