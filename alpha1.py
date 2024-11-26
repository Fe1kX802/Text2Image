from PIL import Image
import numpy as np

def letters_to_ascii(input_string):
        ascii_values = []
        for char in input_string:
            ascii_value = ord(char)
            ascii_values.append(ascii_value)
        return ascii_values

def convert(inputText):
    array = [None] * len(inputText)
    try:
        array = letters_to_ascii(inputText)
        print(f"ASCII коды: {array}")
    except ValueError as e:
        print(e)

def create_image_from_array(data, output_file='output.png'):
    # Проверка, что все числа в массиве находятся в диапазоне от 0 до 255
    data = np.clip(data, 0, 255).astype(np.uint8)

    # Создаем изображение с одной строкой высоты и x пикселей ширины
    height = 1
    width = len(data)
    array = [None] * len(data)
    
    # Создаем новое изображение
    image = Image.new('RGB', (width, height))

    # Заполняем изображение пикселями
    image.putdata([tuple(data[i:i+3]) for i in range(0, len(data), 3)])

    # Сохраняем изображение
    image.save(output_file)
    print(f"Изображение сохранено как {output_file}")

# Пример использования
if __name__ == '__main__':
    # Пример массива из чисел, который будет преобразован в RGB коды
    input_string = input("Input text: ")
    array = [None] * len(input_string)
    convert(input_string)
    #array = [None] * len(data)
    #array = [255, 0, 0, 0, 255, 0, 0, 0, 255, 255, 255, 255, 0, 255, 255]
    
    # Если длина массива не кратна 3, дополним его нулями
    if len(array) % 3 != 0:
        array += [0] * (3 - (len(array) % 3))

    create_image_from_array(array)
