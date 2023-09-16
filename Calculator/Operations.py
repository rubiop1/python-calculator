class Operations:

    def add (num1, num2):
        return num1 + num2

    def less(num1, num2):
        return num1 - num2

    def times(num1, num2):
        return num1*num2

    def div(num1, num2):
        return num1/num2

    def exp(num, exp):
        result = 1
        for x in range(exp):
            result = result * num
        return  result



