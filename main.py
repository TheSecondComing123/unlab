from interpreter import interprete
from tokenizer import tokenize
from parse import parse
from context import Context
import argparse

parser = argparse.ArgumentParser(description="CLI for Excuting Noxan")

# (file name not supported yet)
parser.add_argument(
    "--code", "-c", type=str, help="optional argument to pass code/file name"
)


def main(code):
    """Main function, which returns output of code"""
    ctx = Context()
    output = interprete(parse(tokenize(code)), ctx)
    if ctx.printed:
        return ctx.print
    else:
        return output


def cli():
    """Fucntion for CLI support"""
    args = parser.parse_args()
    if args.code:
        print(main(args.code))
    else:
        shell()


def shell():
    while True:
        code = input(">>> ")
        if code == ":quit:" or code == ":exit:":
            break
        print(main(code))


if __name__ == "__main__":
    cli()
