import enum
import re


class TokenType(enum.Enum):
    NUMBER = "number"
    MATHOP = "mathop"
    ADD = "add"


class TokenRe(enum.Enum):
    NUMBER_RE = r"\d"
    MATHOP_RE = r"[+\-*/]"


class Token:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"Token(name={self.name}, value={self.value})"


def tokenize(text):
    tokens = []
    for ind, char in enumerate(text):
        if re.match(TokenRe.NUMBER_RE.value, char):
            numind = ind
            num = ""
            try:
                while re.match(TokenRe.NUMBER_RE.value, text[numind]):
                    num += text[numind]
                    numind += 1
            except IndexError:
                pass

            tokens.append(Token(TokenType.NUMBER, int(num)))
        elif re.match(TokenRe.MATHOP_RE.value, char):
            if char == "+":
                tokens.append(Token(TokenType.ADD, char))

    return tokens


print(tokenize("+4 49"))
