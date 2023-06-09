import tkinter as tk
import os
from tkinter import filedialog
from PIL import Image

img_file_formats = [".png", ".jpeg", ".jpg", ".bmp", ".tiff"]

output_dir = os.path.join(os.getcwd(), 'compressed')

def isBigFile(filename_with_path):
    file_size = os.path.getsize(filename_with_path)
    if file_size > 10 * 1024 * 1024:
        return True
    else:
        return False

def displayFileSize(filename_with_path):
    file_size = os.path.getsize(filename_with_path)
    # 格式化成以'M'为单位
    file_size = '{:.2f}'.format(file_size / 1024 / 1024)
    return file_size

def compressImg(filename_with_path, filename):
    expectedSize = 10 * 1024 * 1024
    currentSize = 11 * 1024 * 1024
    default_quality = 85
    while currentSize > expectedSize:
        output_path = os.path.join(output_dir, filename)
        with Image.open(filename_with_path) as img:
            img.save(output_path, optimize=True, quality=default_quality)
            default_quality -= 10
            currentSize = os.path.getsize(output_dir)


def browse_folder():
    # 获取文件夹路径
    folder_path = filedialog.askdirectory()
    # print("Selected folder:", folder_path)
    for filename in os.listdir(folder_path):
        filename_with_path = os.path.join(folder_path, filename)
        if os.path.isfile(filename_with_path) and \
            os.path.splitext(filename)[1] in img_file_formats and \
               isBigFile(filename_with_path) :
            compressImg(filename_with_path, filename)
            
            # print(filename)
            # 读取文件
            # with open(os.path.join(folder_path, filename), 'r') as f:
            #     file_content = f.read()

            # 判断文件是否大于10M
            
        # if os.path.isfile(os.path.join(folder_path, filename)):
        #     print(os.path.splitext(filename)[1])
            

root = tk.Tk()
# root.withdraw()

button = tk.Button(text="Choose Folder", command=browse_folder)
button.pack()

# root.geometry("500x300")

root.mainloop()