class DivisionByNull(Exception):
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    @property
    def divide_by_null(self):
        try:
            return self.numerator / self.denominator
        except:
            return f'Division by zero error'


check = DivisionByNull(100, 10)
print(check.divide_by_null)
check2 = DivisionByNull(100, 0)
print(check2.divide_by_null)
check3 = DivisionByNull(100, 0.1)
print(check3.divide_by_null)