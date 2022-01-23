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
    parse_list = []
    tokens = deque(tokens)

    while tokens:
        token = tokens.popleft()

        if token.name == TokenType.FUNCTION:
            if not tokens: # account for there not being anything
                           # after this token by just breaking the loop
                parse_list.append(token)
                break
            arity = elements[token.value][0]
            temp = parse(tokens)  # We call parse on the remaining token
            # list so that it groups whatever is left - this works
            # because complete functions (functions and a complete
            # number of constants/nilads) form single units, and non-
            # complete functions (functions and a non-complete number
            # of constants/nilads) can use those single units.
            parse_list.append([token] + temp[:arity])  # Add a list of
            # this token plus however many grouped tokens the arity
            # requires
            parse_list += temp[arity:]  # add the rest of the parsed
            # tokens
            break
            # exit the loop because everything is parsed.
        elif token.name == TokenType.NUMBER:
            parse_list.append(token) # Numbers don't need anything else

    return parse_list


if __name__ == "__main__":
    print(parse(tokenize("+1 +3 +4 5")))
    print(parse(tokenize("+1 +3 4 +5 6")))
