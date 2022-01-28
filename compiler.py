from tokenizer import tokenize, Token, TokenType
from elements import elements
from parse import parse
from helper_functions import to_python_index


class Interpreter:
    def __init__(self, tokens):
        self.tokens = tokens
        self.position = []

    def main(self, tokens):
        self.position.append(0)

        for index, sub in enumerate(tokens):
            self.position[-1] = index
            if isinstance(sub, list):
                val = self.main(sub)
                del self.position[-1]

                exec(to_python_index("self.tokens", self.position[:-1]) + f"={val[0]}")

        try:
            func = tokens[0]
            args = tokens[1:]
            val = elements[func.value][1](args)
            exec(to_python_index("self.tokens", self.position[:-1]) + f"={val}")

            return self.tokens
        except:
            return self.tokens


if __name__ == "__main__":
    interpreter = Interpreter(parse(tokenize("+1 2")))
    print(interpreter.main(interpreter.tokens))

    interpreter = Interpreter(parse(tokenize("+1 +2 3")))
    print(interpreter.main(interpreter.tokens))

    interpreter = Interpreter(parse(tokenize("++1 2 7")))
    print(interpreter.main(interpreter.tokens))

    interpreter = Interpreter(parse(tokenize("++1 2+3 4")))
    print(interpreter.main(interpreter.tokens))
