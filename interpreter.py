from elements import elements
from helper import Literals
from typing import Any


class Interprete:
    def main(self, tokens: list[Any], ctx):

        if len(tokens) == 1 and not callable(tokens[0]):
            # If tokens is a single literal wrapped in a list, the interpreter will crash
            # So if tokens[0] is a literal, then unwrap it
            tokens = tokens[0]

        self.output = []
        main_output = self.interprete(tokens, ctx)

        self.output.insert(0, main_output) if main_output else None
        return self.output

    def interprete(self, tokens: list[Any], ctx) -> Any:
        if type(tokens) is list:  # If tokens are grouped
            if type(tokens[0]) is list:  # If the func part actually is a list
                # then there are more tokens in the stack to be outputted
                # Example: "+2 3 4"
                for token in tokens:
                    output = self.interprete(token, ctx=ctx)
                    self.output.append(output)
            else:
                func = tokens[0]

                # Exit if func does not exist
                if not func:
                    return [None]

                args = []  # Interprete every argument, recursive case
                for token in tokens[1:]:
                    args.append(self.interprete(token, ctx=ctx))

                args.append(ctx)

                # Call func on every interpreted argument
                output = func(*list(args))
                return output

        else:
            return tokens
