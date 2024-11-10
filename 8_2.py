from PIL import Image
import os

d = {
    'Новый год': "C:\\Users\\annku\\Downloads\\открытка_нг.jpg",
    'День рождения': "C:\\Users\\annku\\Downloads\\открытка_др.jpg",
    '8 марта': "C:\\Users\\annku\\Downloads\\открытка_8_марта.jpg"
}

holiday = input('Введите ваш праздник: ')

if holiday in d:
    file_name = d[holiday]

    if os.path.exists(file_name):
        image = Image.open(file_name)
        image.show()
    else:
        print("Файл открытки не найден.")
else:
    print("Такой праздник не найден.")