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
for file_name in os.listdir(input_folder):
    if file_name.endswith(".jpg"):
        input_path = os.path.join(input_folder, file_name)
        output_path = os.path.join(output_folder, "filtered_" + file_name)
        process_image(input_path, output_path, filter_type)

print("Изображения обработаны и сохранены в новую папку!")