from PIL import Image

image = Image.open("C:/Users/Аннф/Desktop/amnyam.jpeg")
width, height = image.size
small_image = image.resize((width // 3, height // 3))
small_image.save("small_" + "amnyam.jpeg")
horizontal_mirror = image.transpose(Image.FLIP_LEFT_RIGHT)
horizontal_mirror.save("horizontal_mirror_" + "amnyam.jpeg")
vertical_mirror = image.transpose(Image.FLIP_TOP_BOTTOM)
vertical_mirror.save("vertical_mirror_" + "amnyam.jpeg")

print("Изображения сохранены!")