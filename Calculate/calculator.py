import math
class Operations:
    def __init__(self, value):
        self.value = value

    @classmethod
    def add(self, num1, num2):
        return (num1 + num2)

    def less(self, num1, num2):
        return num1 - num2

    def times(self, num1, num2):
        return num1 * num2

    def div(self, num1, num2):
        return num1 / num2

    def exp(self, num, exp):
        result = 1
        for x in range(exp):
            result = result * num
        return result