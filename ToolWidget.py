from abc import ABC, abstractmethod


class ToolWidget(ABC):
    """" Abstract class for further implementations of a tool in the toolbox.

    A standardized abstract base class that defines all tools which will be used and implemented in the Tool Box.
    This abstract class contains the basic functions needed for a tool and allows for easy storage and manipulation of
    all tools.

    """

    @abstractmethod
    def calc(*args):
        """"" The calculate method which executes the calculation done by the tool.

        The calc method can take a variable number of args so as not to restrict input for each tool. For example,
        calculating the area of a circle needs only one input while a physics or chemistry tool might need many inputs
        to calculate the final result. Each implementation will specify in what order the arguments are to be entered
        (e.g Calculating the area of a rectangular prism: length in arg[0], width in arg[1], and height in arg[2]).
        As a rule, every implementation is guaranteed to work correctly if len(args) == [the number of args specified
        by the implementation].

        To reiterate, each implementation of a ToolWidget must clearly state the number and type of arguments to
        facilitate a clear contract between the client and implementation so that the return value of the implementation
        is correct.

        Returns:
            The result of the calculation performed by the tool.

        """
        pass
