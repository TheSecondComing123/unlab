from parser import parse
from tokenizer import tokenize
from elements import elements


def compile(tokens):
    for i, sub in enumerate(tokens.copy()):
        if isinstance(sub[0], list):
            val = compile(sub[0])
        else:
            func = sub[0]
            args = sub[1:]
            val = elements[func.value][1](args)
            tokens[i] = val

    return tokens


if __name__ == "__main__":
    print(compile(parse(tokenize("+1 23"))))
