from PIL import Image

image_path = "C:\\Users\\annku\\Downloads\\kitty.jpg"
image = Image.open(image_path)
width, height = image.size
print("Размер изображения: {}x{}".format(width, height))
print("Формат изображения: {}".format(image.format))
print("Цветовая модель: {}".format(image.mode))
image.show()