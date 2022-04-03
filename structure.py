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


def get_bracket_index(token_list):
    balance = 1
    index = 0
    for index in range(len(token_list)):
        if token_list[index].value == "{":
            balance += 1
        if token_list[index].value == "}":
            balance -= 1
        if balance == 0:
            return index

    return index


def structure_forLoop(token_list: list[Token], main=True):
    if main:
        tokens_copy = list(token_list)
        for index, token in enumerate(token_list):
            if token.value == "↹" and token_list[index + 1].value == "{":
                tokens_copy.insert(index + 1, Token(TokenType.NUMBER, 10))

        token_list = list(tokens_copy)

    output_lst = []
    index = 0
    while index < len(token_list):
        token = token_list[index]

        if token.value == "↹":

            bracket_index = get_bracket_index(token_list[3 + index :])
            output_lst += [
                ForLoop(
                    token_list[index + 1],
                    structure_forLoop(
                        token_list[3 + index : bracket_index + 3 + index], main=False
                    ),
                )
            ]

            index += bracket_index + 3
        else:
            output_lst.append(token)

        index += 1

    return output_lst


def structure(tokens):
    return structure_forLoop(tokens)


if __name__ == "__main__":
    print(structure(tokenize("2↹4{1↹{9}}5")))
