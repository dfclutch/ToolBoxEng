from ToolWidget import ToolWidget
import csv


class AtomicMass(ToolWidget):

    @staticmethod
    def calc(*args):
        """""
        Calculates the atomic mass of a compound based on a chemical formula.
        Args:
            arg[0]: chemical formula, must be formatted with capital letters for the first letter of each element and
            subsequent letters in lower case

        Returns:
            An int representation of the atomic mass, if improperly formatted an error message

        """

        # handle errors
        if len(args) > 1:
            return "Incorrect formatting"
        else:
            # create elements dictionary
            elements = {}
            with open('AtomicMass.csv') as csvfile:
                el = csv.reader(csvfile, delimiter=",")
                for row in el:
                    elements[row[0]] = float(row[1])

            # parse formula
            formula = args[0]
            contents = []
            for i in formula:
                if not i.isnumeric():
                    if i.isupper():
                        contents.append(i)
                    elif i.islower():
                        first_letter = contents.pop(-1)
                        contents.append(first_letter + i)
                else:
                    if contents[-1].isnumeric():
                        first_digit = contents.pop(-1)
                        contents.append(first_digit + i)
                    else:
                        contents.append(i)

            # calculate mass
            total = 0
            i = 0
            while i < len(contents):
                c = contents[i]
                current_element = ""
                current_multiple = 1
                if not c.isnumeric():
                    current_element = c
                    if len(contents) > i + 1 and contents[i + 1].isnumeric():
                        current_multiple = int(contents[i + 1])
                        i += 1
                current_mass = elements.get(current_element)
                total = total + current_mass * current_multiple
                i += 1
            return total
