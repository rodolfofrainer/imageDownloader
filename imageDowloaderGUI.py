import os
import requests
import threading
import tkinter as tk
from tkinter import filedialog

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}

class ImageDownloaderGUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title('Image Downloader')
        self.create_widgets()

    def create_widgets(self):
        self.select_file_label = tk.Label(
            self.master, text='Select a .txt file containing image URLs:')
        self.select_file_label.pack()
        self.select_file_button = tk.Button(
            self.master, text='Select file', command=self.select_file)
        self.select_file_button.pack()

        self.save_to_label = tk.Label(
            self.master, text='Select a directory to save the images:')
        self.save_to_label.pack()
        self.save_to_button = tk.Button(
            self.master, text='Select directory', command=self.select_directory)
        self.save_to_button.pack()

        self.download_button = tk.Button(
            self.master, text='Download images', command=self.download_images, state='disabled')
        self.download_button.pack()

    def select_file(self):
        self.filename = filedialog.askopenfilename(
            filetypes=[('Text files', '*.txt')])
        if self.filename:
            self.select_file_label.config(
                text=f'Selected file: {self.filename}')
            self.download_button.config(state='normal')

    def select_directory(self):
        self.directory = filedialog.askdirectory()
        if self.directory:
            self.save_to_label.config(
                text=f'Selected directory: {self.directory}')

    def download_images(self):
        with open(self.filename, 'r') as file:
            links = file.readlines()

        threads = []
        for index, link in enumerate(links):
            thread = threading.Thread(
                target=self.download_image, args=(link, index))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        self.download_button.config(state='disabled')
        self.select_file_label.config(
            text='Select a .txt file containing image URLs:')
        self.save_to_label.config(
            text='Select a directory to save the images:')
        self.select_file_button.config(state='normal')
        self.save_to_button.config(state='normal')

    def download_image(self, url, index):
        page = requests.get(url.strip(), headers=HEADERS)
        filename = os.path.join(self.directory, f'{index}.jpg')
        with open(filename, 'wb') as file:
            file.write(page.content)
