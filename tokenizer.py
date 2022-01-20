import enum
import re


class TokenType(enum.Enum):
    NUMBER = "number"
    FUNCTION = "function"


class RegEx(enum.Enum):
    NUMBER = r"\d"
    FUNCTION = r"\D"
    IGNORE_TOKEN = r" "


class Token:
    def __init__(self, name: TokenType, value: str):
        self.name = name
        self.value = value

    def __repr__(self):
        return f'Token(name={self.name}, value="{self.value}")'


def tokenize(text: str) -> list[Token]:
    tokens = []
    current_number = False
    number = ""

    for ind, char in enumerate(text):
        if not re.match(RegEx.NUMBER.value, char):
            if current_number:
                tokens.append(Token(TokenType.NUMBER, number))
                current_number = False
                number = ""
        if re.match(RegEx.IGNORE_TOKEN.value, char):
            next

        elif re.match(RegEx.FUNCTION.value, char):
            tokens.append(Token(TokenType.FUNCTION, char))

        elif re.match(RegEx.NUMBER.value, char):
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
    print(tokenize("+1 +3 4"))
