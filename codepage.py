FUNCTIONS = ["+", "-", "×", "÷", "ⁱ", "g", "¶", "Đ", "Ŋ", "Ƣ", "!", "¡", "□"]

INDICATORS = ["↹", "{", "}"]

codepage = FUNCTIONS + INDICATORS
codepage += [chr(x) for x in range(32, 126+1)]

assert len(codepage) <= 256
