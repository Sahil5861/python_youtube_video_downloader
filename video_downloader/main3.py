import tkinter as tk
from tkinter import ttk
from pytube import YouTube
from threading import Thread

def download_video():
    link = input_field.get()
    destination_point = r'C:\Users\Sahil Khan\Desktop\youtube downloads'  # Change this to your desired destination folder

    def download_thread():
        try:
            yt = YouTube(link)
            yd = yt.streams.get_highest_resolution()
            yd.download(destination_point)
            result_label.config(text=f'Download Successful!\nSaved at: {destination_point}')
        except Exception as e:
            result_label.config(text=f'Download Failed!\nError: {str(e)}')
        finally:
            loading_indicator.stop()
            download_button.config(state=tk.NORMAL)

    loading_indicator.start()
    download_button.config(state=tk.DISABLED)
    thread = Thread(target=download_thread)
    thread.start()

win = tk.Tk()
win.title('Youtube Video Downloader')
win.geometry('500x250')

label = ttk.Label(win, text='Youtube Video Downloader', font='Helvetica 16 bold')
label.grid(row=0, column=0, pady=10)

input_label = ttk.Label(win, text='Paste your Youtube Link Here:')
input_label.grid(row=1, column=0, pady=5)

input_field = ttk.Entry(win, width=50)
input_field.grid(row=1, column=1, pady=5)

download_button = ttk.Button(win, text='Download Video', command=download_video)
download_button.grid(row=2, column=0, columnspan=2, pady=10)

loading_indicator = ttk.Progressbar(win, mode='indeterminate', length=300)
loading_indicator.grid(row=3, column=0, columnspan=2, pady=10)

result_label = ttk.Label(win, text='', font='Helvetica 10 italic')
result_label.grid(row=4, column=0, columnspan=2, pady=5)

win.mainloop()
