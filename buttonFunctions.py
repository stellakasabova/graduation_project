from tkinter import *
from getImageData import getTagLabels, getCaption
from uploadToBlob import uploadBlob


def cycleImages(image_number, caption_label, image_label, image_frame, images, image_paths, tag_frame, tag_arr):
    # Delete old tags
    for i in range(0, len(tag_arr)):
        tag_arr[i].grid_forget()

    image_label.grid_forget()
    image_label = Label(image_frame, image=images[image_number - 1])
    image_label.grid(row=0, column=0, columnspan=3)

    caption_label.grid_forget()
    caption_label = Label(image_frame, text=getCaption(image_paths[image_number - 1]))
    caption_label.grid(row=1, column=1)

    # Display new tags
    tag_arr = getTagLabels(image_paths[image_number - 1], tag_frame)
    for j in range(0, len(tag_arr)):
        tag_arr[j].grid(row=j, column=0)

    button_back = Button(image_frame, text="<<", command=lambda: cycleImages(image_number - 1,
                                                                             caption_label,
                                                                             image_label,
                                                                             image_frame,
                                                                             images,
                                                                             image_paths,
                                                                             tag_frame,
                                                                             tag_arr))
    button_forward = Button(image_frame, text=">>", command=lambda: cycleImages(image_number + 1,
                                                                                caption_label,
                                                                                image_label,
                                                                                image_frame,
                                                                                images,
                                                                                image_paths,
                                                                                tag_frame,
                                                                                tag_arr))

    if image_number == len(images):
        button_forward = Button(image_frame, text=">>", state=DISABLED)

    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)


def archive(path):
    archive_window = Toplevel(height=300, width=300)

    zip_name_label = Label(archive_window, text="What name should the directory be archived under? (Please separate "
                                                "words with underscores, not spaces)")
    zip_name_label.pack()
    zip_name_input = Entry(archive_window)
    zip_name_input.pack()

    submit_button = Button(archive_window, text="Submit", command=lambda: uploadBlob(path, zip_name_input.get()))
    submit_button.pack()
