from parse import parse
from elements import elements
from tokenizer import tokenize


def compile(tokens):
    for i, sub in enumerate(tokens.copy()):
        if isinstance(sub[2], list):
            val = compile(sub[0])
        else:
            func = sub[0]
            args = sub[1:]
            val = elements[func.value][1](args)
            tokens[i] = val

    return tokens[0]


if __name__ == "__main__":
    print(compile(parse(tokenize("+1 2"))))
