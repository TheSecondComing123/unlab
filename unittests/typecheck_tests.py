import unittest
from helper import typecheck


class MyTestCase(unittest.TestCase):
    def test_typecheck(self):
        self.assertEqual(typecheck([1, 2, 3], [int, int, int]), True)
        self.assertEqual(typecheck(["abc", [1, 2], 9.0], [str, list, float]), True)
        self.assertEqual(typecheck([[]], [str, int, float, tuple, list]), list)


if __name__ == '__main__':
    unittest.main()
