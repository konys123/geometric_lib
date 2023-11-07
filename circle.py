import math
import unittest

def area(r):
    '''принимает число r, возвращает площадь круга с радиусом r'''
    return math.pi * r * r


def perimetr(r):
    '''принимает число r, возвращает периметр круга с радиусом r'''
    return 2 * math.pi * r


class CircleTest(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area(self):
        res = area(1)
        self.assertEqual(res, math.pi)

    def test_zero_perimetr(self):
        res = perimetr(0)
        self.assertEqual(res, 0)
