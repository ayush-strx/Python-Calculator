from calculate import Calculator


def main():
    calc = Calculator()

    while True:
        print("\n========== Simple Calculator ==========")
        print("0. Exit")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Percentage")
        print("6. Power")
        print("7. Modulus")
        print("8. Floor Division")
        print("9. Square Root")
        print("10. Factorial")
        print("========================================")

        try:
            choice = input("\nEnter your choice: ")

            if choice == "0":
                print("\nThank you for using the calculator!")
                break

            elif choice == "1":
                num_1 = float(input("Enter the first number: "))
                num_2 = float(input("Enter the second number: "))
                print(f"\nResult: {num_1} + {num_2} = {calc.add(num_1, num_2)}")

            elif choice == "2":
                num_1 = float(input("Enter the first number: "))
                num_2 = float(input("Enter the second number: "))
                print(f"\nResult: {num_1} - {num_2} = {calc.subtract(num_1, num_2)}")

            elif choice == "3":
                num_1 = float(input("Enter the first number: "))
                num_2 = float(input("Enter the second number: "))
                print(f"\nResult: {num_1} × {num_2} = {calc.multiply(num_1, num_2)}")

            elif choice == "4":
                num_1 = float(input("Enter the first number: "))
                num_2 = float(input("Enter the second number: "))
                print(f"\nResult: {num_1} ÷ {num_2} = {calc.divide(num_1, num_2)}")

            elif choice == "5":
                num_1 = float(input("Enter the number: "))
                num_2 = float(input("Enter the percentage: "))
                print(f"\nResult: {num_2}% of {num_1} = {calc.percentage(num_1, num_2)}")

            elif choice == "6":
                num_1 = float(input("Enter the base number: "))
                num_2 = float(input("Enter the exponent: "))
                print(f"\nResult: {num_1} ** {num_2} = {calc.power(num_1, num_2)}")

            elif choice == "7":
                num_1 = float(input("Enter the first number: "))
                num_2 = float(input("Enter the second number: "))
                print(f"\nResult: {num_1} mod {num_2} = {calc.modulus(num_1, num_2)}")

            elif choice == "8":
                num_1 = float(input("Enter the first number: "))
                num_2 = float(input("Enter the second number: "))
                print(f"\nResult: {num_1} // {num_2} = {calc.floor_division(num_1, num_2)}")

            elif choice == "9":
                num = float(input("Enter the number: "))
                print(f"\nResult: √{num} = {calc.square_root(num)}")

            elif choice == "10":
                num = float(input("Enter the number: "))
                print(f"\nResult: {num}! = {calc.factorial(num)}")

            else:
                print("\nPlease enter a valid choice (0-10).")

        except ValueError:
            print("\nInvalid input. Please enter numeric values.")


if __name__ == "__main__":
    main()