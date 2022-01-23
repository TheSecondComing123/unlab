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


def parse(token_list: list[Token]):
    """Main parse function"""
    group = []
    ungrouped_tokens = 0
    in_function = False
    parse_list = []
    tokens = deque(token_list)
    ind = 0

    while tokens:
        token = tokens.popleft()
        ind += 1

        if token.name == TokenType.FUNCTION:
            if ungrouped_tokens == 0:  # If function is not nested in another one
                ungrouped_tokens = elements[token.value][0]
                in_function = True
                group.append(token)
            elif ungrouped_tokens > 0:  # If function is nested
                c_tokens = tokens.copy()
                c_tokens.appendleft(token)  # Make copy of tokens with the current token

                parsed = parse(list(c_tokens))

                length = len(list(flatten(parsed)))  # Get the length of parsed

                for _ in range(length):
                    tokens.popleft() if tokens else None  # For every token parsed, pop from main token list

                for sub_group in parsed:
                    group.append(sub_group)  # Append every token/group to group

                in_function = False
                ungrouped_tokens = 0

        if token.name == TokenType.NUMBER:
            if not in_function:
                parse_list.append(token)

            # If in function and the last token to be grouped
            elif in_function and ungrouped_tokens == 1:
                group.append(token)
                ungrouped_tokens -= 1
                in_function = False
                parse_list.append(group)
                group = []

            else:  # If in function
                group.append(token)
                ungrouped_tokens -= 1

    if group:
        parse_list.append(group)

    return parse_list


if __name__ == "__main__":
    print(parse(tokenize("+1+3+4 5")))
    print(parse(tokenize("+1+3 4+5 6")))
