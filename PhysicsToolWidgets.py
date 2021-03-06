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
            'White 9': 9,
            'Black 0': 0
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


class VoltageDrop(ToolWidget):

    @staticmethod
    def calc(*args):
        """""
        Calculates the voltage drop over resistors in a simple series circuit.
        Args:
            args[0]: Voltage of power source
            args[1]: list with resistance of each resistor e.g [22, 18, 44]
        """

        voltage = float(args[0])
        res_list = args[1]
        resistors = []

        for i in res_list:
            if i.isnumeric():
                if resistors[-1].isnumeric():
                    num = resistors.pop(-1)
                    resistors.append(num + i)
                else:
                    resistors.append(i)
            else:
                resistors.append(i)
        temp = []
        for j in resistors:
            if j.isnumeric():
                temp.append(int(j))

        resistors.clear()
        resistors = temp
        total_resistance = sum(resistors)

        current = voltage / total_resistance

        output = {}

        for j in range(0, len(resistors)):
            drop = current * resistors[j]
            string = str(resistors[j]) + "Ω resistor:"
            output[string] = " %.2f volts" % drop

        return output


class AmpChange(ToolWidget):

    @staticmethod
    def calc(*args):
        """""
        Calculates the change in amperage over resistors in a simple parallel circuit.
        Args:
            args[0]: Voltage of power source
            args[1]: list with voltage of each resistor e.g [22, 18, 44]
        """

        voltage = float(args[0])
        res_list = args[1]

        resistors = []

        for i in res_list:
            if i.isnumeric():
                if resistors[-1].isnumeric():
                    num = resistors.pop(-1)
                    resistors.append(num + i)
                else:
                    resistors.append(i)
            else:
                resistors.append(i)
        temp = []
        for j in resistors:
            if j.isnumeric():
                temp.append(int(j))

        resistors.clear()
        resistors = temp

        output = {}

        for i in range(0, len(resistors)):
            change = voltage / resistors[i]
            string = str(resistors[i]) + "Ω resistor"
            output[string] = str(change) + " amps"

        return output
