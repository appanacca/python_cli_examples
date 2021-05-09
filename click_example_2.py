import click
from PIL import Image


@click.command()
@click.option("-i", "--input",
                    help="Input image path",
                    type=str,
                    required=True)
@click.option("-o", "--output",
                    help="Output image path",
                    type=str,
                    required=True)
@click.option("--heigth",
                    help="Height of the output image",
                    type=int,
                    default=256)
@click.option("--width",
                    help="Width of the output image",
                    type=int,
                    default=256)
def resize(input: str, heigth: int, width: int, output: str) -> None:
    """Resize an image."""
    img = Image.open(input)
    img_resized = img.resize(width, heigth).convert('RGB')
    img_resized.save(output, "JPEG")


if __name__ == "__main__":
    resize()


