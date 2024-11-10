from PIL import Image

image = Image.open("C:\\Users\\annku\\Downloads\\kitty.jpg")
width, height = image.size
small_image = image.resize((width // 3, height // 3))
small_image.save("small_" + "kitty.jpg")
horizontal_mirror = image.transpose(Image.FLIP_LEFT_RIGHT)
horizontal_mirror.save("horizontal_mirror_" + "kitty.jpg")
vertical_mirror = image.transpose(Image.FLIP_TOP_BOTTOM)
vertical_mirror.save("vertical_mirror_" + "kitty.jpg")

print("Изображения сохранены!")