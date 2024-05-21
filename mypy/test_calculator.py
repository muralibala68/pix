import unittest

import calculator


class MyTestCase(unittest.TestCase):
    def test_square_two(self):
        self.assertEqual(calculator.square(2), 4)

    def test_square_three(self):
        self.assertEqual(calculator.square(3), 9)

    def test_square_zero(self):
        self.assertEqual(calculator.square(0), 0)


if __name__ == '__main__':
    unittest.main()
