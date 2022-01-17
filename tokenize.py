import enum


class TokenType(enum.Enum):
    NUMBER = "number"
    STRING = "string"
    FLOAT = "float"
    LIST = "list"
    DICT = "dict"


class Token:
    def __init__(self, name, value):
        self.name = name
        self.value = value
