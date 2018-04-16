from ToolWidget import ToolWidget
import math
import MathSciConstants


class Add(ToolWidget):
    """
        Add class that implements adding two numbers together
    """
    def calc(*args):
        """"
        Calculates x + y
        Args:
            arg[0]: x
            arg[1]: y
        Returns:
            x + y
        """
        x = args[0]
        y = args[1]
        return x + y


class Power(ToolWidget):
    """"" Power class that implements a power function.
    """

    def calc(*args):
        """""
        Calculates x^y
        Args:
            arg[0]: x
            arg[1]: y
        Returns:
            x^y
        """

        x = args[0]
        y = args[1]
        return math.pow(x, y)


class CircleArea(ToolWidget):
    def calc(*args):
        """""
                Calculates area of a circle
                Args:
                    arg[0]: radius of circle
                Returns:
                    pi * radius^2
                """
        radius = args[0]
        return MathSciConstants.pi * math.pow(radius, 2)
