import enum
import re
from elements import elements

from typing import List


class TokenType(enum.Enum):
    """Class for all Tokens"""

    NUMBER = "number"
    FUNCTION = "function"


class RegEx(enum.Enum):
    """Regex helping class for IsType"""

    NUMBER = r"\d"
    IGNORE_TOKEN = r" "


class IsType:
    """Class to check which token a string is"""

    @staticmethod
    def number(char: str):
        return bool(re.match(RegEx.NUMBER.value, char))

    @staticmethod
    def function(char: str):
        return char in list(elements.keys())

    @staticmethod
    def ignore_token(char: str):
        return bool(re.match(RegEx.IGNORE_TOKEN.value, char))


class Token:
    """Token class"""

    def __init__(self, name: TokenType, value: str):
        self.name = name
        self.value = value

    def __repr__(self):
        return f'Token(name={self.name}, value="{self.value}")'


def tokenize(text: str) -> List[Token]:
    tokens = []
    current_number = False
    number = ""

    for char in text:
        if not IsType.number(char):
            if current_number:
                tokens.append(Token(TokenType.NUMBER, number))
                current_number = False
                number = ""

        if IsType.ignore_token(char):
            continue

        elif IsType.function(char):
            tokens.append(Token(TokenType.FUNCTION, char))

        elif IsType.number(char):
            if not current_number:
                current_number = True
                number += char
            else:
                number += char

    if current_number:
        tokens.append(Token(TokenType.NUMBER, number))

    return tokens


if __name__ == "__main__":
    print(tokenize("+7 59*89 / 207"))
    print(str(tokenize("+1 +3 4")))
