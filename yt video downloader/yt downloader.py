from tkinter import *  # pip install tkinter
from PIL import Image, ImageTk  # pip install pillow
import pywhatkit  # pip install pywhatkit
import pytube  # pip install pytube
import time  # pip install time
import ctypes  # pip install ctype
from pytube import YouTube

ctypes.windll.shcore.SetProcessDpiAwareness(1)
root = Tk()
root.resizable(0, 0)  # window size can't me maximize
root.geometry("400x300")  # window size
root.title("YouTube Downloader")
root.config(background="#222222")
p1 = PhotoImage(file='YD_GUI.png')  # gui logo
root.iconphoto(0, p1)


def click(*args):
    youtube.delete(0, 'end')  # to delete placeholder text


def play():
    # print(f"{video_name.get()}")
    pywhatkit.playonyt(f"{video_name.get()}")
    label_playing = Label(root, text="Playing...", bg="#222222", fg="White")
    label_playing.place(x=150, y=200)


def download():
    video_link = (f"{video_name.get()}")
    yt = pytube.YouTube(video_link)
    video = yt.streams.first()

    # path where video will get saved
    video.download("C:\\Users\\Technical Jaideep\\PycharmProjects\\python programs")
    # video.download("----------path-----------------------------")
    label_downloaded = Label(root, text="Downloaded", bg="#222222", fg="White")
    label_downloaded.place(x=150, y=200)


youtube_image = Image.open("youtube.png")
youtube_image = youtube_image.convert("RGB")
youtube_image = youtube_image.resize((200, 50), Image.ANTIALIAS)
youtube_image = ImageTk. PhotoImage(youtube_image)

label_image = Label(root, image=youtube_image, bg="#222222")
label_image.place(x=100, y=10)

label_heading = Label(root, text="YouTube Downloader",
                      bg="#222222", fg="white", font="Arial 20 bold")
label_heading.place(x=35, y=75)

video_name = StringVar()
youtube = Entry(root, textvariable=video_name, width=30, font=(
    "Arial", 10), bg="Black", fg="White", borderwidth=5, insertbackground="White")
youtube.insert(5, 'Enter video title/url:- ')
youtube.bind("<Button-1>", click)
youtube.place(x=60, y=130)


# label_text = Label(root, text="Search", bg="#222222", fg="White",font="Arial 10 bold")
# label_text.place(x=10, y=123)


play_button = Button(root, text="Play", bd=1, bg="#00FFFF",
                     font=("Arial", 10), command=play,)
play_button.place(x=75, y=180)

download_button = Button(root, text="Downlaod", bd=1, bg="#00FFFF", font=(
    "Arial", 10), command=download, relief=FLAT)
download_button.place(x=260, y=180)
label_username = Label(root, text="Jaideep Singh", bg="#222222", fg="white")
label_username.place(x=10, y=250)


root.mainloop()