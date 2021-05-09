import typer
from PIL import Image


def resize(input: str = typer.Option(..., "--input", "-i", help="Input image path"),
           heigth: int = typer.Option(256, help="Height of the output image"), 
           width: int  = typer.Option(256, help="Width of the output image"), 
           output: str  = typer.Option(..., "--output", "-o", help="Output image path")) -> None:
    """Resize an image."""
    img = Image.open(input)
    img_resized = img.resize((width, heigth)).convert('RGB')
    img_resized.save(output, "JPEG")


if __name__ == "__main__":
    typer.run(resize)


