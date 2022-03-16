from functions import *
from typing import Callable


class Element:
    def __init__(self, *, arity: int, func: Callable):
        self.arity = arity
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)


elements = {
    "+": Element(arity=2, func=Add),
    "-": Element(arity=2, func=Sub),
    "×": Element(arity=2, func=Mul),
    "÷": Element(arity=2, func=TrueDiv),
    "ⁱ": Element(arity=2, func=Power),
    "g": Element(arity=0, func=lambda *x: g),
    # g (and other constants) must be a lambda because the interpreter tries to call it
    "¶": Element(arity=1, func=Print),
    "Đ": Element(arity=1, func=SumDigits),
    "Ŋ": Element(arity=0, func=GeneralInput),
    "Ƣ": Element(arity=2, func=Mod),
    "!": Element(arity=1, func=ExclamationMark),
    "¡": Element(arity=1, func=InversExclamation),
    "□": Element(arity=1, func=HollowSquare),
    "i": Element(arity=2, func=Index)
}
