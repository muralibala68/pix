from PIL import Image
from typing import List

image_paths: List[str] = ['./boy1.jpg', './boy2.jpg']

images: List[Image] = []
for image_path in image_paths:
    image: Image = Image.open(image_path)
    images.append(image)

image_output_path: str = './output.gif'
images[0].save(image_output_path, save_all=True, append_images=images[1:], loop=0, duration=500)

print(f"GIF file {image_output_path} created")


