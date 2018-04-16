import unittest
import MathToolWidgets
import math

class TestMathMethods(unittest.TestCase):

    def testSquare(self):
        expected = 4
        result = MathToolWidgets.Power.calc(2, 2)
        self.assertEqual(result, expected)

    def testCube(self):
        expected = 8
        result = MathToolWidgets.Power.calc(2, 3)
        self.assertEqual(result, expected)

    def testZero(self):
        expected = 1
        result = MathToolWidgets.Power.calc(2123, 0)
        self.assertEqual(result, expected)

    def testInsanePower(self):
        for x in range(1, 1000):
            for y in range(1, 100):
                expected = math.pow(x, y)
                result = MathToolWidgets.Power.calc(x, y)
                self.assertEqual(result, expected)

    def testArea1(self):
        radius = 1
        expected = math.pi
        result = MathToolWidgets.CircleArea.calc(radius)
        self.assertAlmostEqual(result, expected)

    def testArea10(self):
        radius = 10
        expected = math.pi * math.pow(radius, 2)
        result = MathToolWidgets.CircleArea.calc(radius)
        self.assertAlmostEqual(result, expected)

    def testArea432169(self):
        radius = 432169
        expected = math.pi * math.pow(radius, 2)
        result = MathToolWidgets.CircleArea.calc(radius)
        self.assertAlmostEqual(result, expected)

    def testIntegral(self):
        func = "x"
        lower = 1
        upper = 2
        expected = 3/2
        result = MathToolWidgets.Integrate.calc(func,lower,upper)
        self.assertEqual(expected, result)

    def testIntegralSquare(self):
        func = "x**2"
        lower = 1
        upper = 2
        expected = 7/3
        result = MathToolWidgets.Integrate.calc(func,lower,upper)
        self.assertEqual(expected, result)

    def testIntegralEuler(self):
        func = "e**x"
        lower = 0
        upper = 5
        expected = (math.e ** 5) - 1
        result = MathToolWidgets.Integrate.calc(func, lower, upper)
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()