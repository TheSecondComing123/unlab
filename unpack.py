from tokenizer import Token, tokenize
from structure import ForLoop
from structure import structure


def unpack_forLoop(tokens):
    unpacked_tokens = []

    for token in tokens:
        if isinstance(token, Token):
            unpacked_tokens.append(token)
        elif isinstance(token, ForLoop):
            for _ in range(token.number.value):
                unpacked_tokens.extend(token.body)

    return unpacked_tokens


def unpack(tokens):
    return unpack_forLoop(tokens)


if __name__ == "__main__":
    print(unpack(structure(tokenize("+2 3↹4{¶1} 5"))))
