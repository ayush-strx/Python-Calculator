import math


class Calculator:

    def add(self, num_1, num_2):
        return num_1 + num_2

    def subtract(self, num_1, num_2):
        return num_1 - num_2

    def multiply(self, num_1, num_2):
        return num_1 * num_2

    def divide(self, num_1, num_2):
        if num_2 == 0:
            return "Division by zero is not allowed."
        return num_1 / num_2

    def percentage(self, num_1, num_2):
        return (num_1 * num_2) / 100

    def power(self, num_1, num_2):
        return num_1 ** num_2

    def modulus(self, num_1, num_2):
        if num_2 == 0:
            return "Modulus by zero is not allowed."
        return num_1 % num_2

    def floor_division(self, num_1, num_2):
        if num_2 == 0:
            return "Floor division by zero is not allowed."
        return num_1 // num_2

    def square_root(self, num):
        if num < 0:
            return "Square root of a negative number is not allowed."
        return math.sqrt(num)

    def factorial(self, num):
        if num < 0 or not num.is_integer():
            return "Factorial is only defined for non-negative integers."
        return math.factorial(int(num))