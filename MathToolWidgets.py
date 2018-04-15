from ToolWidget import ToolWidget
import math
import MathSciConstants


class Power(ToolWidget):
    def calc(*args):
        x = args[0]
        y = args[1]
        return math.pow(x, y)


class CircleArea(ToolWidget):
    def calc(*args):
        radius = args[0]
        return MathSciConstants.pi * Power.calc(radius, 2)
