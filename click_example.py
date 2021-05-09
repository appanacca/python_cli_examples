import click
from app import resize


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
def cli(input, heigth, width, output):
    """Resize an image."""
    resize(input, heigth, width, output)


if __name__ == "__main__":
    cli()


