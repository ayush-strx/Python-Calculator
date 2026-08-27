from calculate import calculator

def main():
    calc = calculator()

    print("<<---------- Simple Calculator ---------->>")

    while True:
        try:
            operand_1 = float(input("Enter the first number: "))
            operand_2 = float(input("Enter the second number: "))

            print("\n========== Choose operations: ==========")
            print(" +  Addition")
            print(" -  Subtraction")
            print(" *  Multiplication")
            print(" /  Division")
            print(" %  Percentage")
            print("==========================================")

            operation = input("\nEnter your choice: ")

            if operation == "+":
                print(f"Result: {operand_1} + {operand_2} = {calc.add(operand_1, operand_2)}")

            elif operation == "-":
                print(f"Result: {operand_1} - {operand_2} = {calc.subtract(operand_1, operand_2)}")

            elif operation == "*":
                print(f"Result: {operand_1} * {operand_2} = {calc.multiply(operand_1, operand_2)}")

            elif operation == "/":
                print(f"Result: {operand_1} / {operand_2} = {calc.divide(operand_1, operand_2)}")

            elif operation == "%":
                print(f"Result: {operand_2}% of {operand_1} = {calc.percentage(operand_1, operand_2)}")

            else:
                print("Please enter a valid operation.")

        except ValueError:
            print("Invalid input. Please enter numeric values.")

        while True:
            choice = input("\nDo you want to continue (y/n): ").lower()     
            if choice == "y":
                break

            elif choice == "n":
                print("Thank you for using the calculator!")
                return

            else:
                print("Please enter only 'y' or 'n'.")
                
if __name__ == "__main__":

    main()