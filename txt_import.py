import tkinter as tk
from tkinter import filedialog

def load_txt_file():
    # Создаем главное окно, которое не будем отображать
    root = tk.Tk()
    root.withdraw()  # Скрываем главное окно

    # Открываем диалоговое окно для выбора файла
    file_path = filedialog.askopenfilename(title="Выберите текстовый файл", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))

    if file_path:  # Если файл был выбран
        with open(file_path, 'r', encoding='utf-8') as file:
            txt_file_text = file.read()  # Читаем содержимое файла в переменную

        #print("Содержимое файла:")
        #print(txt_file_text)  # Выводим содержимое файла в консоль

        return txt_file_text  # Возвращаем содержимое

if __name__ == "__main__":
    txt_file_text = load_txt_file()
