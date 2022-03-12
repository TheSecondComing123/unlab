import unittest, init

from interpreter import run


class MyTestCase(unittest.TestCase):
    def test_numops(self):
        self.assertEqual(run("+1 1"), [2])
        self.assertEqual(run("-2 1"), [1])
        self.assertEqual(run("×2 3"), [6])
        self.assertEqual(run("÷10 5"), [2.0])
        self.assertEqual(run("ⁱ2 3"), [8])
        self.assertEqual(run("Ƣ8 2"), [0])
        self.assertEqual(run("Đ999"), [27])

    def test_constants(self):
        self.assertEqual(run("g"), ["Hello, World!"])


if __name__ == "__main__":
    unittest.main()
