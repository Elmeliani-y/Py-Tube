import os
from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.font import Font
import yt_dlp
import threading

# Set up the main window
window = Tk()
window.config(background="#333")
window.geometry("500x400")
window.title("YouTube Saver to MP3")

# Custom font styling
header_font = Font(family="Arial", size=16, weight="bold")
label_font = Font(family="Arial", size=12)

# Header
header_label = Label(window, text="YouTube MP3 Downloader", fg="white", bg="#333", font=header_font)
header_label.pack(pady=20)

# URL entry label and field
url_label = Label(window, text="Enter YouTube Video URL:", fg="white", bg="#333", font=label_font)
url_label.pack(pady=5)
url_entry = Entry(window, width=50, font=("Arial", 10))
url_entry.pack(pady=5)

# Directory selection label and button
dir_label = Label(window, text="Select Save Directory:", fg="white", bg="#333", font=label_font)
dir_label.pack(pady=5)
dir_entry = Entry(window, width=50, font=("Arial", 10))
dir_entry.pack(pady=5)

def choose_directory():
    directory = filedialog.askdirectory()
    dir_entry.delete(0, END)
    dir_entry.insert(0, directory)

dir_button = Button(window, text="Choose Directory", command=choose_directory, bg="#FF5733", fg="white")
dir_button.pack(pady=5)

# Loading label (initially hidden)
loading_label = Label(window, text="Downloading, please wait...", fg="yellow", bg="#333", font=label_font)

# Download function with threading
def start_download():
    video_url = url_entry.get()
    save_directory = dir_entry.get()

    if not video_url or not save_directory:
        messagebox.showerror("Input Error", "Please provide both a video URL and a save directory.")
        return

    loading_label.pack(pady=10)  # Show loading label
    download_thread = threading.Thread(target=download_audio, args=(video_url, save_directory))
    download_thread.start()

def download_audio(video_url, save_directory):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(save_directory, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': True,  # Suppress verbose yt-dlp output
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        messagebox.showinfo("Success", "Download completed successfully!")
    except Exception as e:
        messagebox.showerror("Download Error", f"An error occurred: {e}")
    finally:
        loading_label.pack_forget()  # Hide loading label

# Download button
download_button = Button(window, text="Download as MP3", command=start_download, bg="#FF5733", fg="white")
download_button.pack(pady=20)

# Start the Tkinter event loop
window.mainloop()
