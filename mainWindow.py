import logging
import os
import PIL

from PIL import ImageTk, Image
from tkinter import *
from tkinter import filedialog

from getImageData import getTagLabels, getCaption
from upload import logInTopLevel
from buttonFunctions import forward, back, archive

root = Tk()
root.title('Application')
root.state("zoomed")

def getImages(path_param):
    logging.basicConfig(level=logging.DEBUG, filename='logs.log', format='%(asctime)s %(levelname)s:%(message)s')
    logger = logging.getLogger(__name__)
    logger.info("Visualizing directory: " + path_param)

    image_paths = []
    images = []
    tag_arr = []

    extensions = ('.JPG', '.jpg', '.JPEG', '.jpeg')
    for file in os.listdir(path_param):
        if file.endswith(extensions):
            path = os.path.join(path_param, file)
            # Azure API only works with images 4MB and under
            if os.path.getsize(path) / (1024 * 1024) < 4:
                image_paths.append(path)

    # Resizes photos for consistent image display
    for image in image_paths:
        temp_image = PIL.Image.open(image)
        temp_image = temp_image.resize((500, 500), PIL.Image.ANTIALIAS)
        temp_resized = ImageTk.PhotoImage(temp_image)
        images.append(temp_resized)

    # Adds frames for structured display of elements
    image_frame = Frame(root, width=700, height=700)
    image_frame.place(anchor=CENTER, relx=.4, rely=.5)
    tag_frame = Frame(root)
    tag_frame.place(anchor=CENTER, relx=.65, rely=.5)

    tag_arr = getTagLabels(image_paths[0], tag_frame)
    for g in range(0, len(tag_arr)):
        tag_arr[g].grid(row=g, column=0)

    image_label = Label(image_frame, image=images[0])
    image_label.grid(row=0, column=0, columnspan=3)

    caption_label = Label(image_frame, text=getCaption(image_paths[0]))
    caption_label.grid(row=1, column=1)

    button_back = Button(image_frame, text="<<", command=back, state=DISABLED)
    button_back.grid(row=1, column=0)
    button_forward = Button(image_frame, text=">>", command=lambda: forward(2,
                                                                            caption_label,
                                                                            image_label,
                                                                            image_frame,
                                                                            images,
                                                                            image_paths,
                                                                            tag_frame,
                                                                            tag_arr))
    button_forward.grid(row=1, column=2)

    archive_button = Button(tag_frame, text="Archive directory", command=lambda: archive(path_param))
    archive_button.grid(row=15)

    upload_zoonar_button = Button(tag_frame, text="Upload to Zoonar",
                                  command=lambda: logInTopLevel(path_param, 'ftp.zoonar.com'))
    upload_zoonar_button.grid(row=16)

    upload_alamy_button = Button(tag_frame, text="Upload to Alamy",
                                  command=lambda: logInTopLevel(path_param, 'upload.alamy.com'))
    upload_alamy_button.grid(row=17)

    dir_button.destroy()

dir_button = Button(root, text="Choose directory", command=lambda: getImages(filedialog.askdirectory()))
dir_button.place(anchor=CENTER, relx=.5, rely=.5)

root.mainloop()
