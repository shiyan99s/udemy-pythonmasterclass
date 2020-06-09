class Multiplication:

    def __init__(self, x):
        self.x = x

    def __mul__(self, other):
        x = self.x + other.x
        return x
    
number_a = Multiplication(4)
number_b = Multiplication(8)

print(number_a * number_b)