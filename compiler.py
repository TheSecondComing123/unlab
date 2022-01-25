def compile(tokens):
    for i, sub in enumerate(tokens):
        for j, e in enumerate(sub):
            if isinstance(e, list):
                val = compile(e)
            else:
                func = sub[0]
                args = sub[1:]
                val = func(args)
            tokens[i][j] = val

    return tokens


