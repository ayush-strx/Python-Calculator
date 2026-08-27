class calculator:
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