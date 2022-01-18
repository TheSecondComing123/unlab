import enum
import re


class TokenType(enum.Enum):
    NUMBER = "number"
    ADD = "add"


class TokenRe(enum.Enum):
    NUMBER_RE = r"\d"
    ADD_RE = r"\+"


class Token:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"Token(name={self.name}, value={self.value})"


_none = lambda x: x


def gettok(name, val, *, converter=_none):
    return Token(name.value, converter(val))


def tokenize(text):
    tokens = []
    for char in text:
        if re.match(TokenRe.NUMBER_RE.value, char):
            tokens.append(gettok(TokenType.NUMBER, char,
                                 converter=int))
        elif re.match(TokenRe.ADD_RE.value, char):
            tokens.append(gettok(TokenType.ADD, char))

    return tokens
