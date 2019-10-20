import unittest


class Calc:
    def add(self, a, b):
        return a + a

    def div(self, a, b):
        if b == 0:
            return None
        else:
            return a / b

    def above(self, a, b):
        if (a > b):
            return True
        else:
            return False
class TestAbove(unittest.TestCase):
    def test_above(self):
        calc = Calc()
        self.assertFalse(calc.above(2,2))
        self.assertFalse(calc.above(1,2))
        self.assertTrue(calc.above(3, 2))
        self.assertTrue(calc.above(3.1, 2.2))
        self.assertEqual(calc.above(-1, -2), True)

    if __name__ == '__main__':
        unittest.main()
