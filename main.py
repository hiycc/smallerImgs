import tkinter as tk
import os
from tkinter import filedialog

file_formats = [".png", ".jpeg", ".jpg", ".bmp", ".tiff", ""]

def browse_folder():
    # 获取文件夹路径
    folder_path = filedialog.askdirectory()
    # print("Selected folder:", folder_path)
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)) and \
            os.path.splitext(filename)[1] in [".png",".jpeg",".jpg",".bmp",".tiff",""] :
            print(filename)
        # if os.path.isfile(os.path.join(folder_path, filename)):
        #     print(os.path.splitext(filename)[1])
            

root = tk.Tk()
# root.withdraw()

button = tk.Button(text="Choose Folder", command=browse_folder)
button.pack()

# root.geometry("500x300")

root.mainloop()