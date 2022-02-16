from functions import *

elements = {
    "+": [2, Add],
    "-": [2, Sub],
    "×": [2, Mul],
    "÷": [2, TrueDiv],
    "ⁱ": [2, Power],
    "g": [0, lambda *x: g],  # g (and other constants) must be a lambda because the interpreter tries to call it
    "¶": [1, Print]
}
