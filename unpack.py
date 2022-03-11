from tokenizer import Token
from structure import ForLoop


def unpack_forLoop(tokens):
    unpacked_tokens = []

    for token in tokens:
        if isinstance(token, Token):
            unpacked_tokens.append(token)
        elif isinstance(token, ForLoop):
            for _ in range(token.number.value):
                unpacked_tokens.extend(token.body)

    return unpacked_tokens
