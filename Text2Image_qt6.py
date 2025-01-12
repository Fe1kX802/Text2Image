# Импортируем необходимые модули
from PIL import Image
from pathlib import Path
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QLabel,
    QFileDialog,
    QComboBox,
    QLineEdit,
    QProgressBar,
    QVBoxLayout,
    QHBoxLayout,
    QMessageBox,
    QScrollArea,
    QSlider,
)
from PyQt6.QtGui import QFont, QIcon, QTransform, QPixmap
from PyQt6.QtCore import Qt
import sys
import time
import os
import subprocess


class Txt2Img(QWidget):
    def __init__(self):
        print("___________                  __     ________    .__                                        ")
        print("\__    ___/  ___  ___  ___ _/  |_   \_____  \   |__|    _____   _____       ____    ____  ")
        print("  |    |   / __ \ \  \/  / \   __\   /  ____/   |  |   /     \  \__  \     / ___\  / __ \ ")
        print("  |    |  \  ___/  >    <   |  |    /       \   |  |  /  Y Y  \  / __ \   /_/    > | ___/ ")
        print("  |____|   \___   >__/\_ \  |__|    \_______ \  |__| (  _|_|   ) (____ /  \___  /  \___  >") 
        print("                                                                          _____/          ")
        super().__init__()

        # Устанавливаем название окна
        self.setWindowTitle("Text 2 Image")

        # Задаем размер окна
        self.resize(230, 300)

        # Создаем основной вертикальный макет
        v_layout = QVBoxLayout(self)

        self.setWindowTitle("Text 2 Image")
        self.setWindowIcon(QIcon(os.path.join('images', 'icon.png')))

        # Заголовок
        title_label = QLabel("Text 2 Image", alignment=Qt.AlignmentFlag.AlignCenter)
        title_font = QFont("Dungeon", 20, QFont.Weight.Bold)
        title_label.setFont(title_font)
        v_layout.addWidget(title_label)

        # Горизонтальный макет для кнопки загрузки файла
        h_load_file_layout = QHBoxLayout()
        load_button = QPushButton("Загрузить")
        load_button.clicked.connect(self.load_text_file)
        h_load_file_layout.addStretch()
        h_load_file_layout.addWidget(load_button)
        h_load_file_layout.addStretch()
        v_layout.addLayout(h_load_file_layout)

        # Поле ввода имени файла
        h_name_layout = QHBoxLayout()
        name_label = QLabel("Имя:")
        self.name_input = QLineEdit("output")
        h_name_layout.addWidget(name_label)
        h_name_layout.addWidget(self.name_input)
        v_layout.addLayout(h_name_layout)

        # Комбо-бокс для выбора расширения файла
        h_extension_layout = QHBoxLayout()
        extension_label = QLabel("Расширение:")
        self.extension_combo_box = QComboBox()
        self.extension_combo_box.addItems(["png", "jpg", "webp", "ico", "bmp"])
        self.extension_combo_box.setCurrentIndex(0)
        h_extension_layout.addWidget(extension_label)
        h_extension_layout.addWidget(self.extension_combo_box)
        v_layout.addLayout(h_extension_layout)

        # Комбо-бокс для выбора типа изображения (цветное/черно-белое)
        h_color_type_layout = QHBoxLayout()
        color_type_label = QLabel("Тип изображения:")
        self.color_type_combo_box = QComboBox()
        self.color_type_combo_box.addItems(["Цветная", "Черно-белая"])
        self.color_type_combo_box.setCurrentIndex(0)
        h_color_type_layout.addWidget(color_type_label)
        h_color_type_layout.addWidget(self.color_type_combo_box)
        v_layout.addLayout(h_color_type_layout)

        # Комбо-бокс для выбора цветового формата (RGB/CMYK)
        h_color_format_layout = QHBoxLayout()
        color_format_label = QLabel("Цветовой формат:")
        self.color_format_combo_box = QComboBox()
        self.color_format_combo_box.addItems(["RGB", "CMYK"])
        self.color_format_combo_box.setCurrentIndex(0)
        h_color_format_layout.addWidget(color_format_label)
        h_color_format_layout.addWidget(self.color_format_combo_box)
        v_layout.addLayout(h_color_format_layout)

        # Прогресс бар
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        v_layout.addWidget(self.progress_bar)

        # Кнопки Старт и Отмена
        h_buttons_layout = QHBoxLayout()
        cancel_button = QPushButton("Отмена")
        cancel_button.clicked.connect(self.close)
        start_button = QPushButton("Старт")
        start_button.clicked.connect(self.start_conversion)
        h_buttons_layout.addWidget(start_button)
        h_buttons_layout.addWidget(cancel_button)
        v_layout.addLayout(h_buttons_layout)

        # Центральный виджет
        self.setLayout(v_layout)

        # Переменные для хранения данных
        self.input_string = ""
        self.color = "Цветная"
        self.color_format = "RGB"

    def loading_done(self):
        pass

    def load_text_file(self):
        """Метод для открытия диалога выбора файла"""
        file_dialog = QFileDialog.getOpenFileName(
            self, "Открыть текстовый файл", "", "Текстовые файлы (*.txt *.md);;Все файлы (*)"
        )
        if file_dialog[0]:
            file_path = Path(file_dialog[0])
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    self.input_string = file.read()
                print(self.input_string)
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Произошла ошибка при чтении файла: {e}")

    def start_conversion(self):
        """Метод для запуска процесса преобразования текста в изображение"""
        if not self.input_string:
            QMessageBox.warning(self, "Предупреждение", "Файл пуст или не был загружен.")
            return

        # Получаем значения из интерфейса
        name = self.name_input.text().strip()
        extension = self.extension_combo_box.currentText()
        self.color = self.color_type_combo_box.currentText()
        self.color_format = self.color_format_combo_box.currentText()

        # Преобразуем строку в массив ASCII значений
        array = []
        try:
            for char in self.input_string:
                ascii_value = ord(char)
                array.append(ascii_value)
        except NameError as e:
            QMessageBox.critical(self, "Ошибка", f"Произошла ошибка при преобразовании строки: {e}")
            return

        # Проверяем длину массива и дополняем его до кратности трем
        if len(array) % 3 != 0:
            array += [0] * (3 - (len(array) % 3))

        # Обновляем прогрессбар
        for count in range(101):
            self.progress_bar.setValue(count)
            QApplication.processEvents()
            time.sleep(0.01)

        # Создаем изображение
        create_image_from_array(array, name, extension, self.color, self.color_format)

        # Показываем сообщение об успешном сохранении
        QMessageBox.information(self, "Успех", f"Изображение успешно создано и сохранено как {name}.{extension}.")

    def closeEvent(self, event):
        """Обработчик закрытия окна"""

        event.accept()

def create_image_from_array(data, name, extension, color, color_format):
    """
    data: Массив данных, представляющий пиксели изображения
    name: Имя файла для сохранения
    extension: Расширение файла
    color: Тип изображения ('Цветная' или 'Черно-белая')
    color_format: Цветовой формат ('RGB' или 'CMYK')
    """
    width = len(data)
    height = 1
    pixels = []

    image = Image.new("RGB", (width, height))

    if color == 'Цветная':
        for i in range(height):
            for j in range(width - 2):
                r = data[j]
                g = data[j + 1]
                b = data[j + 2]
                pixels.append((r, g, b))
    elif color == 'Черно-белая':
        for i in range(height):
            for j in range(width):
                r = data[j]
                g = data[j]
                b = data[j]
                pixels.append((r, g, b))

    image.putdata(pixels)
    if color_format == 'CMYK':
        image = image.convert('CMYK')
    image.save(f"{name}.{extension}")
    print(f"Изображение сохранено как {name}.{extension}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Txt2Img()
    ex.show()
    sys.exit(app.exec())