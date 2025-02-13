from calculator_Real_Subject import Calculator
from calculator import CalculatorAbstract


class CalculatorProxy(CalculatorAbstract):
    def __init__(self):
        self._calculator = Calculator()  # Correctly instantiate the Calculator class

    def add(self, a, b):
        """Returns the sum of a and b."""
        return self._calculator.add(a, b)

    def sub(self, a, b):
        """Returns the difference between a and b."""
        return self._calculator.sub(a, b)

    def mul(self, a, b):
        """Raises NotImplementedError since multiplication is not allowed."""
        raise NotImplementedError("Multiplication is not allowed in the free version.")

    def div(self, a, b):
        """Raises NotImplementedError since division is not allowed."""
        raise NotImplementedError("Division is not allowed in the free version.")

    def power(self, a, b):
        """Raises NotImplementedError since exponentiation is not allowed."""
        raise NotImplementedError("Exponentiation is not allowed in the free version.")
