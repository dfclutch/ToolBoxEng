import unittest
import PhysicsToolWidgets


class TestPhysicsMethods(unittest.TestCase):

    def testResistorBandSimple(self):
        expected = '11Ω ±1%'
        result = PhysicsToolWidgets.ResistorBand.calc('Brown 1', 'Brown 1', 'Black x1 Ω', 'Brown  ±1%')
        self.assertEqual(expected, result)

    def testResistorBandMega(self):
        expected = '52MΩ ±2%'
        result = PhysicsToolWidgets.ResistorBand.calc('Green 5', 'Red 2', 'Blue x1 MΩ', 'Red   ±2%')
        self.assertEqual(expected, result)

    def testDrop(self):
        expected = ""
        result = PhysicsToolWidgets.VoltageDrop.calc(9, [2, 3, 5])
        self.assertEqual(expected, result)

    def testChange(self):
        expected = ""
        result = PhysicsToolWidgets.AmpChange.calc(9, [2, 3, 5])
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
