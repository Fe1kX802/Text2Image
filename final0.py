from PIL import Image
import numpy as np
import tkinter as tk
from tkinter import filedialog

def create_image_from_array(data, output_file='output.png'):
    data = np.clip(data, data, data).astype(np.uint8)

    height = 1
    width = len(data)

    image = Image.new('RGB', (width, height))

    image.putdata([tuple(data[i:i+3]) for i in range(0, len(data), 3)])

    image.save(output_file)
    print(f"Изображение сохранено как {output_file}")

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(title="Выберите текстовый файл", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
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
