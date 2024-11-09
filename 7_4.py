def watermarkadd():
    from PIL import Image
    import os

    def add_watermark(image_path, watermark_path, output_folder):
        image = Image.open(image_path)
        watermark = Image.open(watermark_path)
        image_width, image_height = image.size
        watermark_width, watermark_height = watermark.size
        scale_factor = min(image_width / 3 / watermark_width, image_height / 3 / watermark_height)
        new_width = int(watermark_width * scale_factor)
        new_height = int(watermark_height * scale_factor)
        watermark_resized = watermark.resize((new_width, new_height))
        position = ((image_width - new_width) // 2, (image_height - new_height) // 2)
        image.paste(watermark_resized, position, watermark_resized)
        output_path = os.path.join(output_folder, os.path.basename(image_path))
        image.save(output_path)

    input_folder = "input_images"
    watermark_path = "watermark.png"
    output_folder = "output_images"

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg"):
            image_path = os.path.join(input_folder, filename)
            add_watermark(image_path, watermark_path, output_folder)
print(watermarkadd())