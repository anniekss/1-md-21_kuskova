from PIL import Image

image_path = "C:\\Users\\annku\\Downloads\\открытка.jpg"
img = Image.open(image_path)

area = (470, 240, 1440, 950)
cropped_img = img.crop(area)
cropped_img.save("обрезанная_открытка.jpg")

print("Изображение успешно обрезано и сохранено.")