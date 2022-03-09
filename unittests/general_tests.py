import unittest
from interpreter import run


class MyTestCase(unittest.TestCase):
    def test_basicops(self):
        self.assertEqual(run("+1 1"), [2])
        self.assertEqual(run("-1 1"), [0])


if __name__ == '__main__':
    unittest.main()
