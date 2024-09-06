def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed."


def module(a, b):
    if b != 0:
        return a % b
    else:
        return "Error: Division by zero is not allowed."


print("\t*** Arithmetic Calculator ***")
print(" 1.Add \n 2.Subtract \n 3.Multiply \n 4.Divide \n 5.Module \n 6.Exit")

while True:
    option = input("Select the operation you want to perform (1-6): ")

    if option == "6":
        print("Exiting.....")
        break

    if option in ["1", "2", "3", "4", "5"]:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if option == "1":
            print(f"Addition of {num1} and {num2} is: {addition(num1, num2)}")
        elif option == "2":
            print(f"Subtraction of {num1} and {num2} is: {subtraction(num1, num2)}")
        elif option == "3":
            print(f"Multiplication of {num1} and {num2} is: {multiplication(num1, num2)}")
        elif option == "4":
            result = division(num1, num2)
            print(f"Division of {num1} and {num2} is: {result}")
        elif option == "5":
            result = module(num1, num2)
            print(f"Module of {num1} and {num2} is: {result}")
    else:
        print("Invalid option....")

    repeat = input("Would you like to do another calculation? (y/n): ")
    if repeat.lower() != "y":
        print("Exiting.....")
        break
