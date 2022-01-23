from tkinter import *
from PIL import ImageTk, Image
from getTags import getTags

root = Tk()
root.geometry("1000x1000")

img1 = Image.open("D:\photos\Kom Trip\IMG_0280.JPG")
img2 = Image.open("D:\photos\Kom Trip\IMG_0302.JPG")
img3 = Image.open("D:\photos\Kom Trip\IMG_0272.JPG")
img4 = Image.open("D:\photos\Kom Trip\IMG_0307.JPG")

img1 = img1.resize((200, 200), Image.ANTIALIAS)
img2 = img2.resize((200, 200), Image.ANTIALIAS)
img3 = img3.resize((200, 200), Image.ANTIALIAS)
img4 = img4.resize((200, 200), Image.ANTIALIAS)

img1_resize = ImageTk.PhotoImage(img1)
img2_resize = ImageTk.PhotoImage(img2)
img3_resize = ImageTk.PhotoImage(img3)
img4_resize = ImageTk.PhotoImage(img4)

def getLabels(path):
    arr = getTags(path)
    labels = []
    for i in range(0, len(arr)):
        lb = Label(root, text="")
        labels.append(lb)

    for j in range(0, len(labels)):
        labels[j].configure(text=arr[j].name)

    return labels

image_paths = ["D:\photos\Kom Trip\IMG_0280.JPG", "D:\photos\Kom Trip\IMG_0302.JPG", "D:\photos\Kom Trip\IMG_0272.JPG", "D:\photos\Kom Trip\IMG_0307.JPG"]
img_list = [img1_resize, img2_resize, img3_resize, img4_resize]

label = Label(image=img1_resize)
label.grid(row=0, column=0, columnspan=3)

label_arr = getLabels(image_paths[0])
for g in range(0, len(label_arr)):
    label_arr[g].grid(row=g, column=0)

def forward(image_number):
    global label
    global button_back
    global button_forward
    global label_arr

    for h in range(0, len(label_arr)):
        label_arr[h].grid_forget()

    label.grid_forget()
    label = Label(image=img_list[image_number-1])

    label_arr = getLabels(image_paths[image_number - 1])
    for k in range(0, len(label_arr)):
        label_arr[k].grid(row=k, column=0)

    button_back = Button(root, text="<<", command=lambda: back(image_number-1))
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))

    if image_number == len(img_list):
        button_forward = Button(root, text=">>", state=DISABLED)

    label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

def back(image_number):
    global label
    global button_back
    global button_forward
    global label_arr

    for u in range(0, len(label_arr)):
        label_arr[u].grid_forget()

    label.grid_forget()
    label = Label(image=img_list[image_number - 1])

    label_arr = getLabels(image_paths[image_number - 1])
    for e in range(0, len(label_arr)):
        label_arr[e].grid(row=e, column=0)

    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))

    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

button_back = Button(root, text="<<", command=back, state=DISABLED).grid(row=1, column=0)
button_forward = Button(root, text=">>", command=lambda: forward(2)).grid(row=1, column=2)

root.mainloop()
