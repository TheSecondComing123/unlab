from tokenizer import tokenize, Token
from elements import elements
from parse import parse
from helper import TokenList


def interprete(tokens: list[Token]) -> TokenList:
    if type(tokens) is list:  # If tokens are grouped
        if len(tokens) == 1 and type(tokens[0]) is list:
            # At the beginning, tokens is a list like [[+, 1, 2]], so
            # just take the first element
            tokens = tokens[0]

        func = elements.get(tokens[0].value)  # Get the lambda of the func part

        # Exit if func does not exist else get the lambda of the element
        func = exit() if func is None else func[1]

        args = map(interprete, tokens[1:])  # Map interprete to each argument

        return func(*list(args))  # Call func on every interpreted argument

    else:  # when tokens is a single integer
        return tokens


if __name__ == "__main__":
    print(interprete(parse(tokenize("+1 3"))))
    print(interprete(parse(tokenize("+1+3 4"))))
    print(interprete(parse(tokenize("++1+3 2 5"))))
