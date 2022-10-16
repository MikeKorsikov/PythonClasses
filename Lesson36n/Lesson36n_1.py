# testing

class Calculator:
    @staticmethod
    def addition(a, b):
        if isinstance(a, int) and isinstance(b, int):
            return a + b
        else:
            return 'Addition Error'

    @staticmethod
    def deduction(a, b):
        if isinstance(a, int) and isinstance(b, int):
            return a - b
        else:
            return 'Deduction Error'

    @staticmethod
    def multiplication(a, b):
        if isinstance(a, int) and isinstance(b, int):
            return a * b
        else:
            return 'Multiplication Error'

    @staticmethod
    def division(a, b):
        if isinstance(a, int) and isinstance(b, int):
            return a / b
        else:
            return 'Division Error'

