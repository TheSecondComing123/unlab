from tokenizer import TokenType
from elements import elements


class Group:
    def __init__(self, tokens):
        self.tokens = tokens

    def __repr__(self):
        return f"Group({self.tokens})"


def parse(tokens):
    FUNCTION = TokenType.FUNCTION
    NUMBER = TokenType.NUMBER

    parse_list = []  # main list
    group = []
    tokens_not_grouped = 0
    in_function = 0

    for token in tokens:
        if token is FUNCTION:
            tokens_not_grouped = elements[token.name][0]
            in_function = 1
            group += token

        if token is NUMBER:
            if not in_function:
                parse_list += token
            elif in_function and tokens_not_grouped == 0:  # all tokens are grouped
                in_function = 0
                parse_list.append(Group(
                    group))  # add the function-argument pair to the group list
            else:
                group += token  # we are in a function that should be grouped
                tokens_not_grouped -= 1  # -1 because then the tokens that should be grouped are reduced by 1
