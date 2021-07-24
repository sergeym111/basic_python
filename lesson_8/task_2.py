class ZeroDivision:
    def __init__(self, divident, divisor):
        self.divident = divident
        self.divisor = divisor

    @staticmethod
    def zero_division(self):
        try:
            return self.divident / self.divisor
        except:
            return f"Деление на ноль невозможно"


div_1 = ZeroDivision(10, 10)
print(div_1.zero_division(div_1))
div_2 = ZeroDivision(10, 0)
print(div_2.zero_division(div_2))