from PIL import Image, ImageFilter
import os
def process_image(input_path, output_path, filter_type):
    image = Image.open(input_path)
    filtered_image = image.filter(filter_type)
    filtered_image.save(output_path)
input_folder = "C:\\Users\\annku\\Downloads\\"
output_folder = "C:\\py.projects\\1-md-21_kuskova\\"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
filter_type = ImageFilter.CONTOUR
allowed_extensions = ['.jpg', '.png']
for file_name in os.listdir(input_folder):
    if os.path.isfile(os.path.join(input_folder, file_name)):
        name, extension = os.path.splitext(file_name)
        if extension.lower() in allowed_extensions:
            input_path = os.path.join(input_folder, file_name)
            output_path = os.path.join(output_folder, "filtered_" + file_name)
            process_image(input_path, output_path, filter_type)

print("Изображения обработаны и сохранены в новую папку!")