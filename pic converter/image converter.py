from datetime import datetime
from tkinter import *
from tkinter.filedialog import *
import tkinter.messagebox as tmsg
from PIL import Image, ImageTk
import tkinter
import ctypes
import os
from tkinter import colorchooser

ctypes.windll.shcore.SetProcessDpiAwareness(1)

root = Tk()
root.title("Image Converter")
root.geometry("800x600")
root.config(background="#626262")
root.resizable(0, 0)
date_string = datetime.now().strftime("%d%m%Y%H%M%S")


def upload_image(*args):
    try:
        open_image = askopenfilename(title="Open File", filetypes=[('All Files', '*.*'),
                                                                   ("PNG Files", "*.png"), ("JPEG", "*.jpeg*")])
        global image_location
        image_location = f"{open_image}"
        image1 = Image.open(image_location)
        image2 = image1.resize((400, 300), Image.ANTIALIAS)
        test = ImageTk.PhotoImage(image2)
        label1 = tkinter.Label(image=test)
        label1.image = test
        label1.pack(side=RIGHT, padx=25)
        import_image['state'] = 'disable'

        status = Label(root, text="You have selected this image",
                       font="Arial 20", fg="White", bg="Black")
        status.place(x=350, y=460)

    except:
        tmsg.showwarning("Error", "No image have been selected")


def convert_to_png():
    filename, file_extension = os.path.splitext(image_location)
    image_name = os.path.basename(filename)
    status = Label(root, text="----",
                   font="Arial 20", fg="White", bg="Black")
    status.place(x=350, y=520)
    Image.open(image_location).save("converted_" + date_string +
                                    f"{image_name}.png")

    status.config(text="Converted 😊")


def convert_to_jpeg():
    filename, file_extension = os.path.splitext(image_location)
    image_name = os.path.basename(filename)
    status = Label(root, text="----",
                   font="Arial 20", fg="White", bg="Black")
    status.place(x=350, y=520)

    try:
        Image.open(image_location).save("converted_" + date_string +
                                        f"{image_name}.jpeg")
        status.config(text="Converted 😊")
    except OSError:
        if Image.open(image_location).mode == "RGBA":
            a = Image.open(image_location)
            a = a.convert("RGB")
            a.save("converted_" + date_string +
                   f"{image_name}.jpeg")
            status.config(text="Converted 😊")


def convert_to_gif():
    filename, file_extension = os.path.splitext(image_location)
    image_name = os.path.basename(filename)
    status = Label(root, text="----",
                   font="Arial 20", fg="White", bg="Black")
    status.place(x=350, y=520)

    Image.open(image_location).save("converted_" + date_string +
                                    f"{image_name}.gif")
    status.config(text="Converted 😊")


def convert_to_pdf():
    filename, file_extension = os.path.splitext(image_location)
    filename, file_extension = os.path.splitext(image_location)
    status = Label(root, text="----",
                   font="Arial 20", fg="White", bg="Black")
    status.place(x=350, y=520)

    a = os.path.basename(filename)
    image_path = f"{image_location}"
    pdf = Image.open(image_path)
    try:
        pdf.save(f"{a}"+date_string+"convert.pdf")
        status.config(text="Converted 😊")
    except:
        if pdf.mode == "RGBA":
            pdf = pdf.convert("RGB")
            pdf.save(f"{a}"+date_string+"convert.pdf")
            status.config(text="Converted 😊")


button_image1 = PhotoImage(file="upload_image_button.png")
button_image2 = PhotoImage(file="convert_to_png.png")
button_image3 = PhotoImage(file="convert_to_jpeg.png")
button_image4 = PhotoImage(file="convert_to_pdf.png")
button_image5 = PhotoImage(file="convert_to_gif.png")


# UPLOAD IMAGE BUTTON-------------------
import_image = Button(root, image=button_image1, borderwidth=10,
                      background="White", command=upload_image)
import_image.place(x=270, y=50)


# CONVERT TO PNG---------------
convert_to_png = Button(root, image=button_image2,
                        borderwidth=5, background="White", command=convert_to_png)
convert_to_png.place(x=20, y=150)

# CONVERT TO JPEG---------------
convert_to_jpeg = Button(root, image=button_image3,
                         borderwidth=3, background="White", command=convert_to_jpeg)
convert_to_jpeg.place(x=20, y=250)


# CONVERT TO PDF---------------
convert_to_pdf = Button(root, image=button_image4,
                        borderwidth=3, background="White", command=convert_to_pdf)
convert_to_pdf.place(x=20, y=350)

# CONVERT TO GIF---------------
convert_to_gif = Button(root, image=button_image5,
                        borderwidth=3, background="White", command=convert_to_gif)
convert_to_gif.place(x=20, y=450)


def choose_color():

    color_code = colorchooser.askcolor(title="Choose color")
    try:
        root.config(background=color_code[1])
    except:
        return


color = Menu(root)

color.add_command(label="never let your work stop",
                  command=choose_color, font=("Verdana", 14))
root.config(menu=color)

label_name = Label(root, text="by Jaideep Singh",
                   font=("Arial 10 bold"), bg="#626262", fg="Black", padx=30)
label_name.place(x=20, y=550)


root.mainloop()