import argparse
from app import resize


parser = argparse.ArgumentParser(description='Resize an image.')
parser.add_argument("-i", "--input",
                    help="Input image path",
                    type=str,
                    required=True)
parser.add_argument("--heigth",
                    help="Height of the output image",
                    type=int,
                    default=256)
parser.add_argument("--width",
                    help="Width of the output image",
                    type=int,
                    default=256)
parser.add_argument("-o", "--output",
                    help="Output image path",
                    type=str,
                    required=True)


if __name__ == "__main__":
    cli_args = parser.parse_args()
    resize(cli_args.input, cli_args.heigth, cli_args.width, cli_args.output)



    """import inspect

    def log_parameters_of_caller():
        caller_frame = inspect.stack()[1].frame
        _, _, _, values = inspect.getargvalues(caller_frame)
        for item in values:
            print(f"{item}: {values[item]}")"""