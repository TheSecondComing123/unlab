import enum
import re


class TokenType(enum.Enum):
    Number = "number"
    Function = "function"


class RegEx(enum.Enum):
    Number = r"\d"
    Function = r"\D"
    IgnoreToken = r" "


class Token:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f'Token(name={self.name}, value="{self.value}")'


def tokenize(text):
    tokens = []
    current_number = False
    number = ""

    for ind, char in enumerate(text):
        if re.match(RegEx.IgnoreToken.value, char):
            next
        elif re.match(RegEx.Number.value, char):
            if not current_number:
                current_number = True
                number += char
            else:
                number += char

        elif re.match(RegEx.Function.value, char):
            tokens.append(Token(TokenType.Function, char))

        if not re.match(RegEx.Number.value, char):
            if current_number:
                tokens.append(Token(TokenType.Number, number))
                current_number = False
                number = ""

    if current_number:
        tokens.append(Token(TokenType.Number, number))

    return tokens


if __name__ == "__main__":
    print(tokenize("+7 59*89 / 207"))
