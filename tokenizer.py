import enum
import re
from codepage import codepage


class TokenType(enum.Enum):
    """Class for all Tokens"""

    NUMBER = "number"
    STRING = "string"
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
        return char in codepage

    @staticmethod
    def ignore_token(char: str):
        return bool(re.match(RegEx.IGNORE_TOKEN.value, char))

    @staticmethod
    def string_delimiter(char: str):
        return char == '"'


class Token:
    """Token class"""

    def __init__(self, name: TokenType, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"Token(name={self.name}, value={repr(self.value)})"  # {self.value} for debugging


def tokenize(text: str) -> list[Token]:
    tokens = []

    current_number = False
    number = ""

    current_string = False
    string = ""

    current_float = False
    float_contents = ""

    for char in text:
        if not IsType.number(char):
            if char == ".":  # decimal point
                float_contents += number + "."
                current_float = True
            if current_number:
                tokens.append(Token(TokenType.NUMBER, int(number)))
                current_number = False
                number = ""
            if current_float:
                float_contents += number
                tokens.append(Token(TokenType.NUMBER, float(float_contents)))
        if not IsType.string_delimiter(char) and current_string:
            string += char

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

        elif IsType.string_delimiter(char):
            if not current_string:
                current_string = True
            else:
                tokens.append(Token(TokenType.STRING, string))
                current_string = False
                string = ""

    if current_number:
        tokens.append(Token(TokenType.NUMBER, int(number)))
    if current_string:
        tokens.append(Token(TokenType.STRING, string))

    return tokens


if __name__ == "__main__":
    print(tokenize("+7 59*89 / 207"))
    print(tokenize("+1 +3 4"))
    print(tokenize('2 "s1" 3 "s2" "s3'))
    print(tokenize("12.34"))
