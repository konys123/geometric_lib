import unittest


def area(a):
    '''принимает число a, возвращает площадь квадрата со стороной a'''
    return a * a


def perimetr(a):
    '''принимает число a, возвращает периметр квадрата со стороной a'''
    return 4 * a


class SquareTest(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area(self):
        res = area(10000)
        self.assertEqual(res, 100000000)

    def test_zero_perimetr(self):
        res = perimetr(0)
        self.assertEqual(res, 0)
