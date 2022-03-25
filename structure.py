"""Structure.py
File for grouping together tokens to structures
"""
from collections import deque
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


def structure_forloop(tokens):
    """
    Groups tokens together to structures
    """

    loop_started = 0
    loop_content = []
    loop_number = Token(TokenType.NUMBER, 10)

    structured_tokens = []
    tokens_deque = deque(tokens)

    while tokens_deque:
        token = tokens_deque.popleft()

        if token.value == "↹":
            loop_started = 1  # stage 1, outside {}
        elif token.value == "{":
            loop_started = 2  # stage 2, inside {}
            close_bracket = 0

            tokens_copy = list(tokens_deque.copy())

            for index in range(len(tokens_copy) - 1, 0, -1):
                tokens_deque.popleft()
                if tokens_copy[index].value == "}":
                    close_bracket = index
                    break

            loop_content = structure_forloop(tokens_copy[:close_bracket])
            print(loop_content)

        elif token.value == "}":  # end of loop
            structured_tokens.append(ForLoop(loop_number, loop_content))

            loop_started = 0
            loop_content = []
            loop_number = Token(TokenType.NUMBER, 10)
        else:
            if loop_started == 1:
                loop_number = token  # loop number
            elif loop_started == 2:
                loop_content.append(token)  # loop body
            elif loop_started == 0:  # outside loop
                structured_tokens.append(token)

    return structured_tokens


def structure(tokens):
    """Function to run all structure operations"""
    return structure_forloop(tokens)


if __name__ == "__main__":
    print(structure(tokenize("↹{1↹{2}}")))
