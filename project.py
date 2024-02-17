import os
from tkinter import *
from tkinter import filedialog
from tkinter.font import Font
from pytube import YouTube

window=Tk()
key=Label(window,text="welcome to our first edition youtube saver :" ,fg="red",bg="black" , font= "myfont" )
key.pack()
window.config(background="black")
window.geometry("500x400")
myfont = Font( family="Arial", size=24, weight="bold")
key2=Label(window,text="enter the link of the music : ",fg="red",bg="black")
key2.pack()
url_entry=Entry(window,width=40)
url_entry.pack()

mp3_label = Label(window, text="Choose MP3 filename:",fg="black",bg="red")
mp3_label.pack()
mp3_entry=Entry(window)
mp3_entry.pack()
def choose_mp3_filename():
        file_path = filedialog.askdirectory()
        mp3_entry.delete(0, END)
        mp3_entry.insert(0, file_path)



mp3_button = Button(window, text="Choose file", command=choose_mp3_filename ,fg="black",bg="red")
mp3_button.pack()

def download_mp3():
    video_url = url_entry.get()
    mp3_filename = mp3_entry.get()

    yt = YouTube(video_url)

    stream = yt.streams.filter(only_audio=True).first()
    stream.download(output_path=mp3_filename)

    video_filename = stream.default_filename

    os.rename(video_filename, mp3_filename)

download_button = Button(window, text="Download as MP3", command=download_mp3 ,fg="black",bg="red")
download_button.pack()
window.title("YouTube saver to mp3")

window.mainloop()
