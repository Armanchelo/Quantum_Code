import PIL.Image
from tkinter import Tk
from tkinter.filedialog import askopenfilename, askdirectory
import os
from time import sleep
import cv2

characters = ['#', 'S', '%', '?', '*', '+', ';', ':', ',', '.', ' ']
characters = [' ', '.', ',', ':', ';', '+', '*', '?', '%', 'S', '#']

def resize(image, height):
    w, h = image.size 
    ratio = w / h
    width = int(ratio * height)
    resized = image.resize((width, height))
    return width, resized

def grey(image):
    grey_image = image.convert('L')
    return grey_image

def pixels_to_ascii(image):
    pixels = image.getdata()
    return ''.join(characters[pixel // 25] for pixel in pixels)

def create_ascii(path, height = 65):
    image = PIL.Image.open(path)
    width, resized_image = resize(image, height)
    grey_image = grey(resized_image)
    ascii_characters = pixels_to_ascii(grey_image)
    pixels = len(ascii_characters)
    ascii_image = '\n'.join(ascii_characters[i : i + width] for i in range(0, pixels, width))
    return ascii_image

def create_frames(path):
    vidcap = cv2.VideoCapture(path)
    count = 1
    frames = []
    while True:
        success,image = vidcap.read()
        if not success: break
        name = f"ascii_video/frame{count}.jpg"
        print(f'image {count}')
        cv2.imwrite(name, image)
        frames.append(create_ascii(name))
        os.remove(name)
        count += 1   
    return frames

Tk().withdraw()
path = askopenfilename()
frames = create_frames(path)
for frame in frames:
    print(frame)
    sleep(1/60)

    

    