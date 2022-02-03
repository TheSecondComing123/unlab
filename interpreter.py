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
        except (KeyError, AttributeError):
            return self.tokens


    @staticmethod
    def interprete(tokens):
        runner = Interpreter(tokens)
        return runner.main(runner.tokens).value


if __name__ == "__main__":
    print(Interpreter.interprete(parse(tokenize("+1 3"))))
    print(Interpreter.interprete(parse(tokenize("+ +1 3 4"))))
    print(Interpreter.interprete(parse(tokenize("+ +1 3 +4 5"))))
