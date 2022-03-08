from tokenizer import Token, TokenType, tokenize
from collections import deque
from helper import Literals
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
                parse_list.append(elements[token.value].func)
                break
            arity = elements[token.value].arity
            temp = parse(list(tokens))  # This works
            # because complete functions (functions and a complete
            # number of constants/nilads) form single units, and non-
            # complete functions (functions and a non-complete number
            # of constants/nilads) can use those single units.
            parse_list.append(
                [elements[token.value].func] + temp[:arity]
            )  # Arity appended to list because function might have args
            parse_list += temp[arity:]
            break  # break because everything is parsed (complete)
        elif token.name in Literals:
            parse_list.append(token.value)  # Literals don't need any special treatment

    return parse_list


if __name__ == "__main__":
    print(parse(tokenize("+1 +3 +4 5")))
    print(parse(tokenize("g")))
