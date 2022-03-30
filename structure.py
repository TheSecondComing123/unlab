from tokenizer import Token, TokenType, tokenize


class ForLoop:
    """
    For loop structure class.

    Syntax:

    ↹number{body}
    (Borrowed from SYNTAX.md)
    """

    def __init__(self, number: Token, body: list):
        self.number = number
        self.body = body

    def __repr__(self):
        return f"ForLoop(number={self.number}, body={self.body})"


def helper(string):
    # Todo: handle errors
    n = 1

    for i in range(len(string)):
        if string[i] == "(":
            n += 1
        if string[i] == ")":
            n -= 1
        if n == 0:
            return i


def structure_forLoop(string):
    result = []
    i = 0

    while i < len(string):
        h = string[i]

        if h == "W":
            body = helper(string[3 + i:])
            result += [(string[i + 1], helper(string[3 + i:body + 3 + i]))]
            i += body + 3
        else:
            result.append([h])

        i += 1

    return result


def structure(tokens):
    return structure_forLoop(tokens)


if __name__ == "__main__":
    print(structure(tokenize("+2 3↹4{¶1} 5")))
    print(structure(tokenize("+2 3↹{¶1} 5")))
