from PIL import Image, ImageFilter

filter_type = ImageFilter.CONTOUR
input_folder = "C:\\Users\\annku\\Downloads\\"
output_folder = "C:\\py.projects\\1-md-21_kuskova\\"
Image_files = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]

for file_name in Image_files:
    image = Image.open(input_folder + file_name)
    filtered_image = image.filter(filter_type)
    new_file_name = output_folder + "filtered_" + file_name
    filtered_image.save(new_file_name)

print('Изображения обработаны и сохранены в новую папку!')