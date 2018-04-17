from ToolWidget import ToolWidget


class ResistorBand(ToolWidget):

    @staticmethod
    def calc(*args):
        """""
        Calculates the value of a resistor based on band color.
        Args:
            arg[0]: color of first band
            arg[1]: color of second band
            arg[2] color of multiplier band
            arg[3] tolerance
        Returns:
            A string with the resistance and tolerance
            e.g 10Ω ±1%

        """

        digits = {
            'Brown 1': 1,
            'Red 2': 2,
            'Orange 3': 3,
            'Yellow 4': 4,
            'Green 5': 5,
            'Blue 6': 6,
            'Violet 7': 7,
            'Gray 8': 8,
            'White 9': 9
        }
        mult = {
            'Black x1 Ω': 1,
            'Brown  x10 Ω': 10,
            'Red  x100 Ω': 100,
            'Orange x1 kΩ': 1,
            'Yellow x10 kΩ': 10,
            'Green x100 kΩ': 100,
            'Blue x1 MΩ': 1,
            'Violet x10 MΩ': 10,
            'Gray x100 MΩ': 100,
            'White x1 GΩ': 1,
            'Gold x.1 Ω': 0.1,
            'Silver x.01 Ω': 0.01
        }

        value = ((digits[args[0]] * 10) + digits[args[1]]) * mult[args[2]]
        ohms = str(args[2])
        ohms = ohms[ohms.find('±')-1:]
        ohms = ohms.strip()
        percent = str(args[3])
        percent = percent[percent.find('±'):]

        return str(value) + ohms + ' ' + percent



