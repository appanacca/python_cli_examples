from fastcore.script import call_parse, Param
from PIL import Image
from typing import Tuple


@call_parse
def resize(input: Param(help="Input image path", type=str),
            heigth:  Param(help="heigth of the output image", type=int, default=256),
            width:  Param(help="with of the output image", type=int, default=256), 
            output:  Param(help="Output image path", type=str)
            ) -> None:
    img = Image.open(input)
    img_resized = img.resize((width, heigth)).convert('RGB')
    img_resized.save(output, "JPEG")
