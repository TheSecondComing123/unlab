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

    group = []
    ungrouped_tokens = 0
    in_function = 0
    parse_list = []
    tokens = deque(tokens)
    ind = 0

    while tokens:
        token = tokens.popleft()
        ind += 1

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

        if token is NUMBER:
            if not in_function:
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
