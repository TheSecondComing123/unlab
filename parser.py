<<<<<<< HEAD
from typing import Iterable

from tokenizer import *
from collections import deque


class Group:
    def __init__(self, tokens):
        self.tokens = tokens

    def __repr__(self):
        return f"Group({self.tokens})"


def flatten(items):
    """Yield items from any nested iterable; see Reference."""
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
            for sub_x in flatten(x):
                yield sub_x
        else:
            yield x


def parse(tokens):
    FUNCTION = TokenType.FUNCTION
    NUMBER = TokenType.NUMBER

=======
from tokenizer import *
from elements import elements


def parse(tokens: list[Token]):
    parse_list = []  # main list
>>>>>>> d8d749f0d2966bad740602bb7ca973de87b1be76
    group = []
    ungrouped_tokens = 0
    in_function = 0
    parse_list = []
    tokens = deque(tokens)
    ind = 0

    while tokens:
        token = tokens.popleft()
        ind += 1

<<<<<<< HEAD
        if token is FUNCTION:
            if ungrouped_tokens == 0:
                ungrouped_tokens = token.get_arity
                in_function = 1
                group += token
            if ungrouped_tokens > 0:
                parsed = parse(tokens[ind-1:])
                length = flatten(parsed)
                for _ in range(len(list(length))):
                    tokens.popleft()
=======
    for token in tokens:
        if token.name == TokenType.FUNCTION:
            tokens_not_grouped = elements[token.value][0]
            in_function = 1
            group.append(token)
>>>>>>> d8d749f0d2966bad740602bb7ca973de87b1be76

        if token.name == TokenType.NUMBER:
            if not in_function:
<<<<<<< HEAD
                parse_list += token
            elif in_function and ungrouped_tokens == 1:
                group += token
                ungrouped_tokens -= 1
                in_function = 0
                parse_list.append(Group(group))
                group = []
            else:
                group += token
                ungrouped_tokens -= 1

    return parse_list
=======
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
>>>>>>> d8d749f0d2966bad740602bb7ca973de87b1be76
