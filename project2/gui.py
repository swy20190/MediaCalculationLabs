from tkinter import *
from seam import delete_seam
from img_energy import calc_energy_matrix
from PIL import Image, ImageTk
import numpy as np


def confirm_btn_handler():
    global im_old
    global im_new
    src_img = ent_filename.get()
    new_width = int(ent_new_width.get())
    new_height = int(ent_new_height.get())
    img = Image.open("data/"+src_img)
    im_old = ImageTk.PhotoImage(img)
    cv_old.create_image(360, 300, image=im_old)
    img = np.array(img)
    old_height, old_width, channel = img.shape
    for i in range(old_width - new_width):
        energy_matrix = calc_energy_matrix(img)
        img = delete_seam(img, energy_matrix, 'vertical')

    for i in range(old_height - new_height):
        energy_matrix = calc_energy_matrix(img)
        img = delete_seam(img, energy_matrix, 'horizontal')

    img = Image.fromarray(np.uint8(img))
    im_new = ImageTk.PhotoImage(img)
    cv_new.create_image(360, 300, image=im_new)
    img.show()
    img.save("output/" + src_img)


root = Tk()
root.title("seam carving")
root.geometry('850x500')
ent_filename = Entry(root, width=100)
ent_filename.place(x=100, y=20, anchor='nw')
ent_new_width = Entry(root, width=100)
ent_new_width.place(x=100, y=50, anchor='nw')
ent_new_height = Entry(root, width=100)
ent_new_height.place(x=100, y=80, anchor='nw')
lab_filename = Label(text="待压缩图片名：")
lab_filename.place(x=10, y=20, anchor='nw')
lab_new_width = Label(text="压缩后宽度：")
lab_new_width.place(x=10, y=50, anchor='nw')
lab_new_height = Label(text="压缩后高度：")
lab_new_height.place(x=10, y=80, anchor='nw')
btn_confirm = Button(root, activebackground='#F83030', command=confirm_btn_handler, fg="#000000", text="确认", width=112)
btn_confirm.place(x=10, y=110, anchor='nw')
lab_old_img = Label(text="压缩前：")
lab_old_img.place(x=10, y=140, anchor='nw')
cv_old = Canvas(root, width=360, height=300, bg='white')
cv_old.place(x=10, y=180, anchor='nw')
im_old = None
im_new = None
lab_new_img = Label(text="压缩后：")
lab_new_img.place(x=440, y=140, anchor='nw')
cv_new = Canvas(root, width=360, height=300, bg='white')
cv_new.place(x=440, y=180, anchor='nw')
root.mainloop()
