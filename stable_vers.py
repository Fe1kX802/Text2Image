from PIL import Image
import numpy as np
import tkinter as tk
from tkinter import filedialog

def create_image_from_array(data, output_file='output.png'):
    width = len(data)
    height = 1
    pixels = []

    image = Image.new("RGB", (width, height))

    for i in range(height):
        for j in range(width - 2):
                r = (data[j])
                g = (data[j+1])
                b = (data[j+2])
                pixels.append((r, g, b))
    #for i in range(height):
    #    for j in range(width):
    #        r = (data[j])
    #        g = (data[j])
    #        b = (data[j])
    #        pixels.append((r, g, b))
    image.putdata(pixels)
    image.save(output_file)
    print(f"Изображение сохранено как {output_file}")

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(title="Выберите текстовый файл", filetypes=(("Text files", "*.txt", "*.md"), ("All files", "*.*")))
    if file_path:  
        with open(file_path, 'r', encoding='utf-8') as file:
            input_string = file.read()  
    print(input_string)
    array = []
    try:
        for char in input_string:
            ascii_value = ord(char)
            array.append(ascii_value)
    except NameError as e:
        print(e)

    #array = list(input_string)

    print(array)
    print(len(array))

    if len(array) % 3 != 0:
        array += [0] * (3 - (len(array) % 3))

    create_image_from_array(array)
