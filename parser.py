from tokenizer import *
from elements import elements


def parse(tokens: list[Token]):
    parse_list = []  # main list
    group = []
    tokens_not_grouped = 0
    in_function = 0

    for token in tokens:
        if token.name == TokenType.FUNCTION:
            tokens_not_grouped = elements[token.value][0]
            in_function = 1
            group.append(token)

        if token.name == TokenType.NUMBER:
            if not in_function:
                parse_list.append(token)

            elif in_function and tokens_not_grouped == 1:  # last token to be grouped
                group.append(token)
                tokens_not_grouped -= 1
                in_function = 0
                parse_list.append(group)

                group = []

            else:  # we are in a function that should be grouped
                group.append(token)
                tokens_not_grouped -= 1

    return parse_list


if __name__ == "__main__":
    print("+1 3")
    print(parse(tokenize("+1 3")), end="\n\n")

    print("+1 3+4 5")
    print(parse(tokenize("+1 3 4+5 6")))
