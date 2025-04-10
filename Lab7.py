import string

class MathUtils:
   
    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    
    def multiply(x, y):
        return x * y

  
    def divide(x, y):
            return x / y
        
    def power(x, y):
        return x ** y


    def mod(x, y):
        return x % y    

import MathUtils
class Calculator:
     def __init__(self):
        self.operators = {
            '+': MathUtils.add,
            '-': MathUtils.subtract,
            '*': MathUtils.multiply,
            '/': MathUtils.divide,
            '**': MathUtils.power,
            '%': MathUtils.mod
        }
        def calculate(self):
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            operator = input("Enter an operator (+, -, *, /, **, %): ")
            
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            operator = input("Enter an operator (+, -, *, /, **, %): ")
            
     def run(self):
        if __name__ == "__main__":
            self.calculate()

