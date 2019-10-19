import math
import time
import unittest
from fraction import Fraction


class FractionTest(unittest.TestCase):
    """Test the methods and constructor of the Fraction class. """

    def test_init(self):
        """
        Test initialize obj.
        :return:
        """
        f = Fraction(3, 5)
        g = Fraction(2, -5)
        self.assertEqual(f.denominator, g.denominator)
        self.assertNotEqual(f.numerator, g.numerator)
        # 0 and -0 is the same according to python math library
        self.assertEqual(Fraction(1, 0), Fraction(1, -0))
        with self.assertRaises(TypeError):
            Fraction('a', 'b')
        with self.assertRaises(TypeError):
            Fraction(denominator=2)
        with self.assertRaises(TypeError):
            Fraction(3.9, 23.4)
        self.assertEqual(Fraction(1, 0), Fraction(5, 0))
        self.assertEqual(Fraction(0, 1), Fraction(0, 4))
        self.assertEqual(Fraction(-1, 0), Fraction(-3, 0))
        self.assertEqual(Fraction(0, 0), Fraction(-0, -0))

    def test_str(self):
        """
        Test Fraction string text in nominator/denominator format. (if denominator = 1 text only display nominator
        same goes to nominator equal to 0).
        :return:
        """
        f = Fraction(3, -1)
        self.assertEqual("-3", f.__str__())
        f = Fraction(0, 5)
        self.assertEqual("0", f.__str__())
        f = Fraction(60, 90)
        self.assertEqual("2/3", f.__str__())
        f = Fraction(1500, 60)
        self.assertEqual("25", f.__str__())
        f = Fraction(1500, 90)
        self.assertEqual("50/3", f.__str__())
        f = Fraction(-80, 20)
        self.assertEqual("-4", f.__str__())
        f = Fraction(36, -60)
        self.assertEqual("-3/5", f.__str__())
        f = Fraction(99)
        self.assertEqual("99", f.__str__())
        f = Fraction(3, 1)
        self.assertEqual("3", f.__str__())
        f = Fraction(0, 0)
        self.assertEqual("0/0", f.__str__())
        f = Fraction(1, 0)
        self.assertEqual("1/0", f.__str__())
        f = Fraction(-1, 0)
        self.assertEqual("-1/0", f.__str__())
        f = Fraction(0, 5)
        self.assertEqual("0",f.__str__())

    def test_multiply(self):
        """
        Test *(Multiply operator).
        :return:
        """
        self.assertEqual(Fraction(6, -25), Fraction(3, 5) * Fraction(2, -5))
        self.assertEqual(Fraction(2, 36), Fraction(1, 12) * Fraction(2, 3))
        self.assertEqual(Fraction(-2, 9), Fraction(2, 3) * Fraction(-1, 3))
        self.assertEqual(Fraction(-2, 9), Fraction(-2, 3) * Fraction(1, 3))
        self.assertEqual(Fraction(-1, 1), Fraction(1, 1) * Fraction(-1, 1))
        self.assertEqual(Fraction(1, 0), Fraction(1, 0) * Fraction(4, 3))
        self.assertEqual(Fraction(-1, 0), Fraction(-1, 0) * Fraction(4, 3))
        self.assertEqual(Fraction(-1, 9), Fraction(3, 9) * Fraction(-3, 9))
        self.assertEqual(Fraction(-1, 0), Fraction(1, 0) * Fraction(-1, 0))
        self.assertEqual(Fraction(0, 0), Fraction(0, 0) * Fraction(-1, 3))
        self.assertEqual(Fraction(0, 0), Fraction(0, 0) * Fraction(1, 0))
        self.assertEqual(Fraction(0, 0), Fraction(0, 0) * Fraction(0, 0))
        self.assertEqual(Fraction(0, 0), Fraction(0) * Fraction(1, 0))
        self.assertEqual(Fraction(0), Fraction(0) * Fraction(999, 9999))

    def test_add(self):
        """
        Test +(addition operator).
        :return:
        """
        # 3/4 = 2/3 + 1/12
        self.assertEqual(Fraction(3, 4), Fraction(1, 12) + Fraction(2, 3))
        self.assertEqual(Fraction(1, 3), Fraction(2, 3) + Fraction(-1, 3))
        self.assertEqual(Fraction(-1, 3), Fraction(-2, 3) + Fraction(1, 3))
        self.assertEqual(Fraction(0, 1), Fraction(1, 1) + Fraction(-1, 1))
        self.assertEqual(Fraction(1, 0), Fraction(1, 0) + Fraction(4, 3))
        self.assertEqual(Fraction(-1, 0), Fraction(-1, 0) + Fraction(4, 3))
        self.assertEqual(Fraction(0, 1), Fraction(3, 9) + Fraction(-3, 9))
        self.assertEqual(Fraction(0, 0), Fraction(1, 0) + Fraction(-1, 0))
        self.assertEqual(Fraction(0, 0), Fraction(0, 0) + Fraction(-1, 3))
        self.assertEqual(Fraction(0, 0), Fraction(0, 0) + Fraction(1, 0))
        self.assertEqual(Fraction(0, 0), Fraction(0, 0) + Fraction(0, 0))

    def test_sub(self):
        """
        Test -(subtraction operator).
        :return:
        """
        # 1/12 - 8/12 = -7/12
        self.assertEqual(Fraction(-7, 12), Fraction(1, 12) - Fraction(2, 3))
        self.assertEqual(Fraction(1, 1), Fraction(2, 3) - Fraction(-1, 3))
        self.assertEqual(Fraction(-1, 1), Fraction(-2, 3) - Fraction(1, 3))
        self.assertEqual(Fraction(2, 1), Fraction(1, 1) - Fraction(-1, 1))
        self.assertEqual(Fraction(1, 0), Fraction(1, 0) - Fraction(4, 3))
        self.assertEqual(Fraction(-1, 0), Fraction(-1, 0) - Fraction(4, 3))
        self.assertEqual(Fraction(2, 3), Fraction(3, 9) - Fraction(-3, 9))
        self.assertEqual(Fraction(1, 0), Fraction(1, 0) - Fraction(-1, 0))
        self.assertEqual(Fraction(0, 0), Fraction(1, 0) - Fraction(1, 0))
        self.assertEqual(Fraction(0, 0), Fraction(0, 0) - Fraction(-1, 3))
        self.assertEqual(Fraction(0, 0), Fraction(0, 0) - Fraction(1, 0))
        self.assertEqual(Fraction(0, 0), Fraction(0, 0) - Fraction(0, 0))

    def test_gt(self):
        """
        Test >(Greater than)
        :return:
        """
        self.assertTrue(Fraction(1, 3) > Fraction(1, 10))
        self.assertTrue(Fraction(-1, 10) > Fraction(-1, 3))
        self.assertTrue(Fraction(9, 17) > Fraction(-1, 8))
        self.assertFalse(Fraction(-10, 12) > Fraction(1, 1))
        self.assertFalse(Fraction(0, 0) > Fraction(0, 0))
        self.assertFalse(Fraction(1, 0) > Fraction(1, 0))
        self.assertTrue(Fraction(1, 0) > Fraction(-1, 0))
        self.assertFalse(Fraction(1, 0) > Fraction(0, 0))

    def test_neg(self):
        """
        Test -(Negation operator)
        :return:
        """
        self.assertEqual(Fraction(2, 5), Fraction(-2, 5).__neg__())
        self.assertEqual(Fraction(7, 5), Fraction(-14, 10).__neg__())
        self.assertEqual(Fraction(-1, 0), Fraction(3, 0).__neg__())
        self.assertEqual(Fraction(5, 0), Fraction(-1, 0).__neg__())
        self.assertEqual(Fraction(0, 0), Fraction(0, 0).__neg__())
        self.assertEqual(Fraction(0), Fraction(0).__neg__())

    def test_eq(self):
        """
        Test ==(Equality operator).
        :return:
        """
        f = Fraction(1, 2)
        g = Fraction(-40, -80)
        h = Fraction(10000, 20001)  # not quite 1/2
        self.assertTrue(f == g)
        self.assertTrue(f.__eq__(g))  # same thing
        self.assertFalse(f == h)
        self.assertFalse(f.__eq__(h))
        # Consider special values like 0, 1/0, -1/0
        self.assertFalse(Fraction(-2, 3).__eq__(Fraction(2, 3)))
        self.assertFalse(Fraction(1, 3).__eq__(Fraction(4, 2)))
        self.assertFalse(Fraction(1, -3).__eq__(Fraction(-4, 7)))
        self.assertFalse(Fraction(2, 3) == (Fraction(2, 5)))
        self.assertFalse(Fraction(3, 5) == (Fraction(2, 5)))
        self.assertTrue(Fraction(0).__eq__(Fraction(0, 3)))
        self.assertTrue(Fraction(1, 0).__eq__(Fraction(6, 0)))
        self.assertFalse(Fraction(1, 0).__eq__(Fraction(-1, 0)))


if __name__ == '__main__':
    unittest.main(verbosity=2)
