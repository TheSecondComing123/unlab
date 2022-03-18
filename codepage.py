FUNCTIONS = []
FUNCTIONS += ["+", "-", "×", "÷", "ⁱ", "g", "¶", "Đ"]
FUNCTIONS += ["Ŋ", "Ƣ", "!", "¡", "□", "i", "s", "t"]
FUNCTIONS += ["h"]

INDICATORS = ["↹", "{", "}"]

codepage = FUNCTIONS + INDICATORS

assert len(codepage) <= 256
