from tokenizer import Token  # Used as a annotation


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


def structure(tokens):
    """
    Groups tokens together to structures
    """

    loop_started = 0
    loop_content = []
    loop_number = None

    structured_tokens = []

    for t in tokens:
        if t.value == "↹":
            loop_started = 1  # stage 1, outside {}
        elif t.value == "{":
            loop_started = 2  # stage 2, inside {}
        elif t.value == "}":  # end of loop
            structured_tokens.append(ForLoop(loop_number, loop_content))

            loop_started = 0
            loop_content = []
            loop_number = None
        else:
            if loop_started == 1:
                loop_number = t  # loop number
            elif loop_started == 2:
                loop_content.append(t)  # loop body
            elif loop_started == 0:  # outside loop
                structured_tokens.append(t)
