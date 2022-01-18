import enum
import re


class TokenType(enum.Enum):
    NUMBER = "number"
    ADD = "add"
    SUB = "sub"
    MUL = "mul"
    DIV = "div"
    NUMBSEP = "numbsep"


class TokenRe(enum.Enum):
    NUMBER_RE = r"\d"
    ADD_RE = r"\+"
    SUB_RE = r"-"
    MUL_RE = r"\*"
    DIV_RE = r"/"
    NUMBSEP_RE = r"\s"


class Token:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"Token(name={self.name}, value={self.value})"


_none = lambda x: x


def gettok(name, val, *, converter=_none):
    return Token(name.value, converter(val))


def handle(regex, c, tokenlist, name, *, converter=_none):
    if re.match(regex.value, c):
        tokenlist.append(gettok(name, c, converter=converter))


def tokenize(text):
    tokens = []
    for char in text:
        handle(TokenRe.NUMBER_RE, char, tokens, TokenType.NUMBER, converter=int)
        handle(TokenRe.ADD_RE, char, tokens, TokenType.ADD)
        handle(TokenRe.SUB_RE, char, tokens, TokenType.SUB)
        handle(TokenRe.MUL_RE, char, tokens, TokenType.MUL)
        handle(TokenRe.DIV_RE, char, tokens, TokenType.DIV)
        handle(TokenRe.NUMBSEP_RE, char, tokens, TokenType.NUMBSEP)

    return tokens


print(tokenize("+1 -99 *4 3"))
