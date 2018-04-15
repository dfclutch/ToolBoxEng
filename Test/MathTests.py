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

    def testInsane(self):
        for x in range(1, 1000):
            for y in range (1, 100):
                expected = math.pow(x, y)
                result = MathToolWidgets.Power.calc(x, y)
                self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()