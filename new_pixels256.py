from PIL import Image

def create_rgb_image(width, height):
    # Создаем новое изображение
    image = Image.new("RGB", (width, height))

    # Заполняем изображение пикселями
    pixels = []
    for i in range(height):
        for j in range(width):
            # Вычисляем индекс пикселя в одномерном виде
            index = i * width + j
            
            # Вычисляем цвет по RGB
            # Каждое значение увеличивается на один и переходит в цикл от 0 до 255
            r = (index % 256)
            #r = 0
            g = (index % 256)
            #g = 0
            b = (index % 256)
            #b = 0
            
            pixels.append((r, g, b))

    # Устанавливаем пиксели в изображение
    image.putdata(pixels)

    # Сохраняем изображение в файл
    image.save("rgb_image.png")
    print("Изображение создано и сохранено как rgb_image.png")

if __name__ == "__main__":
    create_rgb_image(256, 256)
