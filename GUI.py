from tkinter import *
from PIL import Image, ImageTk
import os
from cv2 import cv2

root = Tk()
# get image path and its label
path = r"E:\MachineLearning\MC-OCR2020\content\data\train_annotations.txt"
f = open(path, "r", encoding="utf-8")
image_list = dict()
img_folder = r"content\data\img"
for line in f.readlines():
    line = line.rstrip().split("\t", 1)
    img_name = line[0].split("/")[-1]
    
    img_path = os.path.join(img_folder, img_name)
    # print(img_path)
    # aaaa
    if len(line) == 1:
        image_list[img_path] = "NULL"
    else:
        image_list[img_path] = line[1]

start = 0
img_url = Label(text = list(image_list.keys())[start])
img_url.grid(row = 0, column = 0, columnspan = 3)

my_img = ImageTk.PhotoImage(Image.open(list(image_list)[start]))
my_label = Label(image = my_img)
my_label.grid(row = 1, column = 0, columnspan = 3)

my_gt = Label(text = image_list[list(image_list.keys())[start]])
my_gt.grid(row = 2, column = 0, columnspan = 3)

# text box
e = Entry(root,width = 50)
e.insert(END, "{}".format(image_list[list(image_list.keys())[start]]))
e.grid(row=3, column=0, columnspan=3)

# button
correctButton = Button(root, text = "correct", command=lambda: correct(2))
# skipButton = Button(root, text = "skip", command=lambda: skip(2))
deleteButton = Button(root, text = "delete", command=lambda: delete(2))

# progress bar
progress_string = "%d/%d" % (start+1, len(list(image_list.keys())))
progress_label = Label(root, text=progress_string, width=10)
progress_label.grid(row=5, column=2, columnspan = 3)

correctButton.grid(row=4, column=2, columnspan = 3)
# skipButton.grid(row=4, column=0, columnspan = 3)
deleteButton.grid(row=4, column=1, columnspan = 3)

root.bind('<Return>', lambda _: correct(2))
root.bind('<Tab>', lambda _: delete(2))

def correct(image_number):
    global my_img
    global my_label
    global img_url
    global correctButton
    global skipButton
    global deleteButton
    global my_gt
    global e
    global progress_label

    info = e.get()
    f = open("clean_labels.txt", "a", encoding="utf-8")
    f.write("{}\t{}\n".format(list(image_list.keys())[image_number-2], info))
    f.close()
    my_label.grid_forget()
    img_url.grid_forget()
    my_gt.grid_forget()
    e.grid_forget()
    progress_label.grid_forget()

    img_url = Label(text = list(image_list.keys())[image_number-1])

    my_img = ImageTk.PhotoImage(Image.open(list(image_list)[image_number-1]))
    my_label = Label(image = my_img)

    my_gt = Label(text = image_list[list(image_list.keys())[image_number-1]])
    my_gt.grid(row = 2, column = 0, columnspan = 3) 
    
    # text box
    e = Entry(root, width = 50)
    e.insert(END, "{}".format(image_list[list(image_list.keys())[image_number-1]]))
    e.grid(row=3, column=0, columnspan=3)

    correctButton = Button(root, text="correct", command=lambda: correct(image_number + 1))
    # skipButton = Button(root, text="skip", command=lambda: skip(image_number + 1))
    deleteButton = Button(root, text="delete", command=lambda: delete(image_number + 1))
    root.bind('<Return>', lambda _: correct(image_number + 1))
    root.bind('<Tab>', lambda _: delete(image_number + 1))

    if image_number == len(list(image_list.keys())):
        correctButton = Button(root, text="correct", state=DISABLED)
        # skipButton = Button(root, text="skip", state=DISABLED)
        deleteButton = Button(root, text="delete", state=DISABLED)
    
    

    # progress bar
    progress_string = "%d/%d" % (image_number, len(list(image_list.keys())))
    progress_label = Label(root, text=progress_string, width=10)
    progress_label.grid(row=5, column=2, columnspan = 3)

    my_label.grid(row = 1, column = 0, columnspan = 3)
    img_url.grid(row = 0, column = 0, columnspan = 3)
    correctButton.grid(row=4, column=2, columnspan = 3)
    # skipButton.grid(row=4, column=0, columnspan = 3)
    deleteButton.grid(row=4, column=1, columnspan = 3)


# def skip(image_number):
#     global my_img
#     global my_label
#     global img_url
#     global correctButton
#     global skipButton
#     global deleteButton
#     global my_gt
#     global e
#     global progress_label

#     f = open("clean_labels.txt", "a", encoding="utf-8")
#     f.write("{}\t{}\n".format(list(image_list.keys())[image_number-2], image_list[list(image_list.keys())[image_number-2]]))
#     f.close()

#     my_label.grid_forget()
#     img_url.grid_forget()
#     my_gt.grid_forget()
#     e.grid_forget()

#     img_url = Label(text = list(image_list.keys())[image_number-1])

#     my_img = ImageTk.PhotoImage(Image.open(list(image_list)[image_number-1]))
#     my_label = Label(image = my_img)

#     my_gt = Label(text = image_list[list(image_list.keys())[image_number-1]])
#     my_gt.grid(row = 2, column = 0, columnspan = 3) 

#     # text box
#     e = Entry(root, width = 50)
#     e.insert(END, "{}".format(image_list[list(image_list.keys())[image_number-1]]))
#     e.grid(row=3, column=0, columnspan=3)
    

#     # progress bar
#     progress_string = "%d/%d" % (image_number, len(list(image_list.keys())))
#     progress_label = Label(root, text=progress_string, width=10)
#     progress_label.grid(row=5, column=2, columnspan = 3)

#     correctButton = Button(root, text="correct", command=lambda: correct(image_number + 1))
#     skipButton = Button(root, text="skip", command=lambda: skip(image_number + 1))
#     deleteButton = Button(root, text="delete", command=lambda: delete(image_number + 1))
#     root.bind('<Return>', lambda _: correct(image_number + 1))

#     if image_number == len(list(image_list.keys())):
#         correctButton = Button(root, text="correct", state=DISABLED)
#         skipButton = Button(root, text="skip", state=DISABLED)
#         deleteButton = Button(root, text="delete", state=DISABLED)
    

#     my_label.grid(row = 1, column = 0, columnspan = 3)
#     img_url.grid(row = 0, column = 0, columnspan = 3)
#     correctButton.grid(row=4, column=2, columnspan = 3)
#     skipButton.grid(row=4, column=0, columnspan = 3)
#     deleteButton.grid(row=4, column=1, columnspan = 3)

def delete(image_number):
    global my_img
    global my_label
    global img_url
    global correctButton
    global skipButton
    global deleteButton
    global my_gt
    global e
    global progress_label


    my_label.grid_forget()
    img_url.grid_forget()
    my_gt.grid_forget()
    e.grid_forget()

    img_url = Label(text = list(image_list.keys())[image_number-1])

    my_img = ImageTk.PhotoImage(Image.open(list(image_list)[image_number-1]))
    my_label = Label(image = my_img)

    my_gt = Label(text = image_list[list(image_list.keys())[image_number-1]])
    my_gt.grid(row = 2, column = 0, columnspan = 3) 
    
    # text box
    e = Entry(root, width = 50)
    e.insert(END, "{}".format(image_list[list(image_list.keys())[image_number-1]]))
    e.grid(row=3, column=0, columnspan=3)

    correctButton = Button(root, text="correct", command=lambda: correct(image_number + 1))
    # skipButton = Button(root, text="skip", command=lambda: skip(image_number + 1))
    deleteButton = Button(root, text="delete", command=lambda: delete(image_number + 1))
    root.bind('<Return>', lambda _: correct(image_number + 1))
    root.bind('<Tab>', lambda _: delete(image_number + 1))

    if image_number == len(list(image_list.keys())):
        correctButton = Button(root, text="correct", state=DISABLED)
        # skipButton = Button(root, text="skip", state=DISABLED)
        deleteButton = Button(root, text="delete", state=DISABLED)

    # progress bar
    progress_string = "%d/%d" % (image_number, len(list(image_list.keys())))
    progress_label = Label(root, text=progress_string, width=10)
    progress_label.grid(row=5, column=2, columnspan = 3)

    my_label.grid(row = 1, column = 0, columnspan = 3)
    img_url.grid(row = 0, column = 0, columnspan = 3)
    correctButton.grid(row=4, column=2, columnspan = 3)
    # skipButton.grid(row=4, column=0, columnspan = 3)
    deleteButton.grid(row=4, column=1, columnspan = 3)



    



root.mainloop()