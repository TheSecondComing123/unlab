from interpreter import run
from context import Context
import argparse

parser = argparse.ArgumentParser(description="CLI for Excuting Noxan")

parser.add_argument("--code", "-c", type=str, help="optional argument to pass code")
parser.add_argument(
    "--file", "-f", type=str, help="optional argument to pass file name"
)


def main(code):
    """Main function, which returns output of code"""
    ctx = Context()
    output = run(code, ctx=ctx)
    if ctx.printed:
        return ctx.print
    else:
        return output[-1]


def cli():
    """Function for CLI support"""
    args = parser.parse_args()
    if args.code:
        print(main(args.code))
    elif args.file:
        print(main(open(args.file).read()))
    else:
        shell()


def shell():
    """
    Interactive shell
    """

    while True:
        code = input(">>> ")
        if code == ":quit:" or code == ":exit:":
            break
        print(main(code))


if __name__ == "__main__":
    cli()
