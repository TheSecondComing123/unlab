from tokenizer import Token, TokenType, tokenize
from collections import deque
from elements import elements


def parse(token_list: list[Token]) -> list[Token]:
    """Main parse function
    Args:
        token_list (list[Token]): Tokenized string, a list of Token elements
    Returns:
        list[Token]: Return parsed list, grouped Token elements
    """
    parse_list = []
    tokens = deque(token_list)

    while tokens:
        token = tokens.popleft()

        if token.name == TokenType.FUNCTION:
            if not tokens:  # account for there not being anything
                # after this token by just breaking the loop
                parse_list.append(token.value)
                break
            arity = elements[token.value][0]
            temp = parse(list(tokens))  # We call parse on the remaining token
            # list so that it groups whatever is left - this works
            # because complete functions (functions and a complete
            # number of constants/nilads) form single units, and non-
            # complete functions (functions and a non-complete number
            # of constants/nilads) can use those single units.
            parse_list.append([token.value] + temp[:arity])  # Add a list of
            # this token plus however many grouped tokens the arity
            # requires
            parse_list += temp[arity:]  # add the rest of the parsed
            # tokens
            break
            # exit the loop because everything is parsed.
        elif token.name == TokenType.NUMBER:
            parse_list.append(token.value)  # Numbers don't need anything else

    return parse_list


if __name__ == "__main__":
    print(parse(tokenize("+1 +3 +4 5")))
    print(parse(tokenize("+1 +3 4 +5 6")))
