from tokenizer import tokenize, Token, TokenType
from elements import elements
from parse import parse


def interprete(tokens: list[Token]) -> Token:
    if type(tokens) is list:
        for token in tokens:
            if type(token) is list:
                func = elements.get(token[0].value)[1]
                args = map(interprete, token[1:])
                result = func(list(args))
            else:
                result = tokens
    else:
        result = tokens

    return result


if __name__ == "__main__":
    print(interprete(parse(tokenize("+1 3"))))
    print(interprete(parse(tokenize("+ +1 3 4"))))
    print(interprete(parse(tokenize("+ +1 3 +4 5"))))
