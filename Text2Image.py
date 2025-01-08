from PIL import Image
import tkinter as tk
from tkinter import filedialog
import PySimpleGUI as sg
from tkinter import messagebox as mb
import time

def create_image_from_array(data, name, extension, color):
    width = len(data)
    height = 1
    pixels = []

    image = Image.new("RGB", (width, height))

    if color == 'Цветная':
        for i in range(height):
            for j in range(width - 2):
                    r = (data[j])
                    g = (data[j+1])
                    b = (data[j+2])
                    pixels.append((r, g, b))
    elif color == 'Черно-белая':
        for i in range(height):
            for j in range(width):
                r = (data[j])
                g = (data[j])
                b = (data[j])
                pixels.append((r, g, b))

    image.putdata(pixels)
    image.save(f'{name}.{extension}')
    print(f"Изображение сохранено как {name}.{extension}")

sg.theme('darkblue17')
layout = [[sg.Titlebar("Txt2Img")],
            [sg.VPush()],
            [sg.Push(), sg.Text('Text2Image', font=('YEARBOOK', 20)), sg.Push()],
            [sg.Push(), sg.Text("Исходный файл: "), sg.Button("Загрузить", size=(10)), sg.Push()],
            [sg.Push(), sg.Text("Имя: "), sg.InputText("output", size=(10)), sg.Push()],
            [sg.Push(), sg.Text("Расширение: "), sg.Combo(['png', 'jpg', 'WebP', 'ico', 'bmp'], default_value='png'), sg.Push()],
            [sg.Push(), sg.Text("Цвет картинки: "), sg.Combo(['Цветная', 'Черно-белая'], default_value='Цветная'), sg.Push()],
            [sg.ProgressBar(100, key='-PROGRESS_BAR-', size=(22, 10), bar_color=('green', 'white'))],
            [sg.VPush()],
            [sg.Button('Отмена', button_color='#613434'), sg.Push(), sg.Button('Старт', button_color='#128700')],
            [sg.VPush()]]

window = sg.Window('Txt2Img', layout, resizable=True)

count = 0
input_string = ''
color = 'Цветная'
name = 'output'

while True:
    event, values = window.read()
    if event == 'Загрузить': 
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename(title="Выберите текстовый файл", filetypes=(("Text files", "*.txt", "*.md"), ("All files", "*.*")))
        if file_path:
            with open(file_path, 'r', encoding='utf-8') as file:
                input_string = file.read()
        print(input_string)

    elif event == 'Старт':
        if input_string == '':
            mb.showerror(title='Text2Image', message='Выбранный файл пустой, или файл не выбран')
        else:
            name = values[0]
            extension = values[1]
            color = values[2]
            
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
            for count in range(100):
                window['-PROGRESS_BAR-'].update(current_count=count)
                time.sleep(0.015)
            create_image_from_array(array, name, extension, color)
            mb.showinfo(title='Text2Image', message=f'Изображение закодировано и сохранено как {name}.{extension}')

    elif event == 'Отмена' or event == sg.WIN_CLOSED:
        break

    else:
        mb.showerror(title='Text2Image', message='Что то сломалось')

window.close()

