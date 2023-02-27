"""Write a python program that accepts a variablenumber of arguments
and a variable number of key-value pair arguments to calculate the
sum of these arguments."""

class Addition:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        
    def calculate_sum(self):
        total = 0
        for arg in self.args:
            total += arg
        for value in self.kwargs.values():
            total += value
        return total

num1 = float(input("num1: "))
num2 = float(input("num2: "))
num3 = float(input("num3: "))
num4 = float(input("num4: "))

final_sum = Addition(a = num1, b = num2, c = num3, d = num4)
result = final_sum.calculate_sum()
print(f"Final Sum: {result}")
