from tkinter import *
from getTags import getTagArray

def forward(image_number, image_label, image_frame, images, image_paths, tag_frame, tag_arr):
    for i in range(0, len(tag_arr)):
        tag_arr[i].grid_forget()

    image_label.grid_forget()
    image_label = Label(image_frame, image=images[image_number - 1])

    tag_arr = getTagArray(image_paths[image_number - 1], tag_frame)
    for j in range(0, len(tag_arr)):
        tag_arr[j].grid(row=j, column=0)

    button_back = Button(image_frame, text="<<", command=lambda: back(image_number-1,
                                                                      image_label,
                                                                      image_frame,
                                                                      images,
                                                                      image_paths,
                                                                      tag_frame,
                                                                      tag_arr))
    button_forward = Button(image_frame, text=">>", command=lambda: forward(image_number+1,
                                                                            image_label,
                                                                            image_frame,
                                                                            images,
                                                                            image_paths,
                                                                            tag_frame,
                                                                            tag_arr))

    if image_number == len(images):
        button_forward = Button(image_frame, text=">>", state=DISABLED)

    image_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

def back(image_number, image_label, image_frame, images, image_paths, tag_frame, tag_arr):
    for i in range(0, len(tag_arr)):
        tag_arr[i].grid_forget()

    image_label.grid_forget()
    image_label = Label(image_frame, image=images[image_number - 1])

    tag_arr = getTagArray(image_paths[image_number - 1], tag_frame)
    for j in range(0, len(tag_arr)):
        tag_arr[j].grid(row=j, column=0)

    button_back = Button(image_frame, text="<<", command=lambda: back(image_number - 1,
                                                                      image_label,
                                                                      image_frame,
                                                                      images,
                                                                      image_paths,
                                                                      tag_frame,
                                                                      tag_arr))
    button_forward = Button(image_frame, text=">>", command=lambda: forward(image_number + 1,
                                                                            image_label,
                                                                            image_frame,
                                                                            images,
                                                                            image_paths,
                                                                            tag_frame,
                                                                            tag_arr))

    if image_number == 1:
        button_back = Button(image_frame, text="<<", state=DISABLED)

    image_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)