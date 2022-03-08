from tokenizer import Token  # Used as a annotation


class ForLoop:
    """
    For loop structure class.

    Syntax:

    ↹number{body}
    (Borrowed from SYNTAX.md)
    """

    def __init__(self, number: Token, body: Token):
        self.number = number
        self.body = body

    def __repr__(self):
        return f"ForLoop(number={self.number}, body={self.body})"


def structure(tokens):
    """
    Groups tokens together to structures
    """

    loop_started = 0
    loop_content = []
    loop_number = None

    for t in tokens:

