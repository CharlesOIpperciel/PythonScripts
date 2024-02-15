from pytube import YouTube
import tkinter as tk
from tkinter import filedialog


def checkValidLink():
    link = input('Enter the a Youtube URL: ')
    if 'youtube' not in link.lower():
        print('Invalid URL\n')
        quit()
    else:
        return link


def downloadVideo(link, saveDir):
    try:
        print('Downloading...\n')
        yt = YouTube(link)
        stream = (yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution())
        stream.download(output_path=saveDir)
        print('Video downloaded successfully!')

    except Exception as e:
        print(e)


def openFileDialog():
    filename = filedialog.askdirectory()
    if filename:
        print(f'\nSelected directory is {filename}\n')
    return filename


def checkValidFolder(link, saveDir):
    if saveDir:
        downloadVideo(link, saveDir)
    else:
        print('Invalid save location\n')


if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()

    checkValidFolder(checkValidLink(), openFileDialog())
