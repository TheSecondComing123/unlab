from tokenizer import tokenize, Token
from elements import elements
from parse import parse
from helper import TokenList
from typing import Union


def interprete(tokens: list[Token]) -> Union[TokenList, None]:
    if type(tokens) is list:  # If tokens are grouped
        if len(tokens) == 1 and type(tokens[0]) is list:
            tokens = tokens[0]

        func = elements.get(tokens[0].value)  #

        # Exit if func does not exist else get the lambda of the element
        if func:
            func = func[1]
        else:
            return

        args = map(interprete, tokens[1:])  # Interprete every argument, recursive case
        return func(*list(args))  # Call func on every interpreted argument

    else:
        return tokens


if __name__ == "__main__":
    print(interprete(parse(tokenize("+1 3"))))
    print(interprete(parse(tokenize("+1+3 4"))))
    print(interprete(parse(tokenize("++1+3 2 5"))))
    print(interprete(parse(tokenize("-2 1"))))
    print(interprete(parse(tokenize("×7 2"))))
    print(interprete(parse(tokenize("÷10 2"))))
    interprete(parse(tokenize("¶+1 ×3 3")))
