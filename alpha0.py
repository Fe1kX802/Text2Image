from PIL import Image

def letters_to_ascii(input_string):
        ascii_values = []
        for char in input_string:
            ascii_value = ord(char)
            ascii_values.append(ascii_value)
        return ascii_values

def convert(inputText):
    try:
        ascii_output = letters_to_ascii(inputText)
        print(f"ASCII коды: {ascii_output}")
    except ValueError as e:
        print(e)

def hex_to_rgb(hex_color):
    # Преобразовать шестнадцатеричный цвет в RGB
    if hex_color.startswith('#'):
        hex_color = hex_color[1:]  # Убираем '#' если он есть
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def create_image(hex_colors):
    # Преобразуем каждый шестнадцатеричный код в RGB
    rgb_colors = [hex_to_rgb(hex_color) for hex_color in hex_colors]

    # Создаем пустое изображение 1x1 пиксель
    img = Image.new('RGB', (1, 1))
    
    # Используем первый RGB цвет для пикселя
    img.putpixel((0, 0), rgb_colors[0])
    
    # Сохраняем изображение в файл
    img.save('output.png')
    print('Изображение сохранено как output.png')

if __name__ == '__main__':
    # Входной массив из трех шестнадцатеричных цветов
    hex_colors_input = ['#FF5733', '#33FF57', '#3357FF']  # Например
    create_image(hex_colors_input)
