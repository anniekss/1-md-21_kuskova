from PIL import Image, ImageDraw, ImageFont
import os

input_folder = "C:\\Users\\annku\\Downloads\\"
image_files = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]
watermark = "Water Mark"

for i in image_files:
    try:
        image_path = os.path.join(input_folder, i)
        image = Image.open(image_path)

        drawing = ImageDraw.Draw(image)

        colour = (255, 255, 255)
        font = ImageFont.truetype("arial.ttf", 36)  # Убедитесь, что шрифт доступен

        drawing.text((0, 0), watermark, fill=colour, font=font)

        output_filename = os.path.join(input_folder, "watermarked_" + os.path.basename(i))
        image.save(output_filename)
        print(f"Водяной знак добавлен к {i} и сохранен как {output_filename}")

    except FileNotFoundError:
        print(f"Файл не найден: {i}")
    except Exception as e:
        print(f"Произошла ошибка при обработке {i}: {e}")

print("Обработка завершена!")