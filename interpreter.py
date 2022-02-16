from elements import elements
from helper import TokenList
from typing import Union


def interprete(tokens: TokenList, ctx) -> Union[TokenList, None]:
    if type(tokens) is list:  # If tokens are grouped
        if len(tokens) == 1 and type(tokens[0]) is list:
            tokens = tokens[0]

        func = elements.get(tokens[0])

        # Exit if func does not exist else get the lambda of the element
        if func:
            func = func[1]
        else:
            return

        args = []  # Interprete every argument, recursive case
        for token in tokens[1:]:
            args.append(interprete(token, ctx=ctx))

        args.append(ctx)

        return func(*list(args))  # Call func on every interpreted argument

    else:
        return tokens
