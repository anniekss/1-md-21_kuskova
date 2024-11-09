from PIL import Image, ImageFilter

filter_type = image.filter(ImageFilter.CONTOUR)
input_folder = "D:/Users/Анна/pythonProject11"
output_folder = "D:/Users/Анна/pythonProject11"
image_files = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]

for file_name in image_files:
    image = Image.open(input_folder + file_name)
    filtered_image = image.filter(filter_type)
    new_file_name = output_folder + "filtered_" + file_name
    filtered_image.save(new_file_name)

print("Изображения обработаны и сохранены в новую папку!")