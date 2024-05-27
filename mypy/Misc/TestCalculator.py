import unittest

import Calculator


class MyTestCase(unittest.TestCase):
    def test_square_two(self):
        self.assertEqual(Calculator.square(2), 4)

    def test_square_three(self):
        self.assertEqual(Calculator.square(3), 9)

    def test_square_zero(self):
        self.assertEqual(Calculator.square(0), 0)


if __name__ == '__main__':
    unittest.main()
