import unittest


def area(a, b):
    '''принимает числа a и b, возвращает площадь прямоугольника со сторонами a и b'''
    return a * b


def perimetr(a, b):
    '''принимает числа a и b, возвращает периметр прямоугольника со сторонами a и b'''
    return (a + b) * 2


class RectangleTest(unittest.TestCase):
    def test_zero_area(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_area(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_zero_perimetr(self):
        res = perimetr(0, 0)
        self.assertEqual(res, 0)
