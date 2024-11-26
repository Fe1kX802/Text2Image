from PIL import Image
import numpy as np
import tkinter as tk
from tkinter import filedialog

def create_image_from_array(data, output_file='output.png'):
    width = len(data)
    height = 1
    pixels = []
    cycle = 0

    image = Image.new("RGB", (width, height))

    for i in range(height):
        for j in range(width):
            if cycle == 0:
                r = (data[j])
                g = 0
                b = 0
                cycle += 1
            elif cycle == 1:
                r = 0
                g = (data[j])
                b = 0
                cycle += 1
            else:
                r = 0
                g = 0
                b = (data[j])
                cycle = 0
            
            pixels.append((r, g, b))
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

    array = []
    try:
        for char in input_string:
            ascii_value = ord(char)
            array.append(ascii_value)
    except NameError as e:
        print(e)
    print(array)
    print(len(array))

    if len(array) % 3 != 0:
        array += [0] * (3 - (len(array) % 3))

    create_image_from_array(array)
