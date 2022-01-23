from typing import Iterable

from tokenizer import *
from collections import deque


def flatten(items):
    """Yield items from any nested iterable; see Reference."""
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
            for sub_x in flatten(x):
                yield sub_x
        else:
            yield x


def parse(tokens):
    group = []
    ungrouped_tokens = 0
    in_function = False
    parse_list = []
    tokens = deque(tokens)
    ind = 0

    while tokens:
        token = tokens.popleft()
        ind += 1

        if token.name == TokenType.FUNCTION:
            if ungrouped_tokens == 0:
                ungrouped_tokens = elements[token.value][0]
                in_function = True
                group.append(token)
            elif ungrouped_tokens > 0:
                c_tokens = tokens.copy()
                c_tokens.appendleft(token)

                parsed = parse(c_tokens)

                length = len(list(flatten(parsed)))

                for _ in range(length):
                    tokens.popleft() if tokens else None

                for sub_group in parsed:
                    group.append(sub_group)

                in_function = False

        if token.name == TokenType.NUMBER:
            if not in_function:
                parse_list.append(token)
            elif in_function and ungrouped_tokens <= 1:
                group.append(token)
                ungrouped_tokens -= 1
                in_function = 0
                parse_list.append(group)
                group = []
            else:
                group.append(token)
                ungrouped_tokens -= 1

    if group:
        parse_list.append(group)

    return parse_list


if __name__ == "__main__":
    print(parse(tokenize("+1+3+4 5")))
    print(parse(tokenize("+1+3 4+5 6")))
