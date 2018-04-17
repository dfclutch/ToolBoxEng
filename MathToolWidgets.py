from ToolWidget import ToolWidget
import sympy
import sympy.parsing.sympy_parser
from sympy.parsing.sympy_parser import standard_transformations, implicit_multiplication_application
import math
import MathSciConstants

transformations = standard_transformations + (implicit_multiplication_application,)


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
    """"" Tool Widget that implements a function that calculates the area of a circle.
    """

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


class Integrate(ToolWidget):

    def calc(*args):
        """""
        Calculates the definite integral of a function with respect to x.
            Args:
                args[0]: A string with the function in it
                args[1]: The lower bound of the integral
                args[2]: The upper bound of the integral
        """

        try:
            x = sympy.symbols('x')

            functionString = str(args[0])

            integrand = sympy.parsing.sympy_parser.parse_expr(functionString, transformations=transformations)

            lower = args[1]
            upper = args[2]

            res = sympy.integrate(integrand, (x, lower, upper))
            return float(res)
        except:
            return "Improperly Formatted Function"
class Derivative(ToolWidget):

    def calc(*args):
        """""
        Calculates the value of the first derivative of a function with respect to x.
            Args:
                args[0]: A string with the function in it
                args[1]: The point at which the derivative should be calculated
        """

        x = sympy.symbols('x')

        functionString = str(args[0])

        differential = sympy.parsing.sympy_parser.parse_expr(functionString, transformations=transformations)

        evalPoint = args[1]

        res = sympy.diff(differential, x)

        return res.evalf(subs={x: evalPoint})
