from PIL import Image, ImageDraw, ImageFont
import os

x,y = 10,10
card_path = "C:\\Users\\annku\\Downloads\\открытка_др2.jpg"

if not os.path.exists(card_path):
    print(f"Файл не найден: {card_path}")
else:
    card = Image.open(card_path)

    name = input("Кого Вы хотите поздравить? ")

    draw = ImageDraw.Draw(card)

    font = ImageFont.truetype("arial.ttf", 50)

    text = name + ", поздравляю!"
    text_color = (255, 0, 0)

    bbox = draw.textbbox((x, y), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    image_width, image_height = card.size

    text_position = (image_width - text_width - 50, image_height - text_height - 50)
    """draw.text(text_position, text, font=font, fill=text_color)"""

    draw.text((x-1, y), text, font=font, fill=text_color)
    draw.text((x+1, y), text, font=font, fill=text_color)
    draw.text((x, y-1), text, font=font, fill=text_color)
    draw.text((x, y+1), text, font=font, fill=text_color)

    draw.text((x, y), text, font=font, fill=text_color)

    card.save("C:\\Users\\annku\\Downloads\\new_открытка_др.png")