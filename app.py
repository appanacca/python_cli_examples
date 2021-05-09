from typing import Tuple
from PIL import Image

def resize(input: str,  heigth: int, width: int, output: str) -> None:
    img = Image.open(input)
    img_resized = img.resize((width, heigth)).convert('RGB')
    img_resized.save(output, "JPEG")
