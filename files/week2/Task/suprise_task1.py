def is_palindrom(user_input):
    temp = user_input[::-1]

    if user_input == "" or user_input == " ":
        print("it's an empty string")
    elif temp == user_input:
        print("This number is palindrom")
    else:
        print("Not a palindrom")


user_input = input("Enter a number to check whether it is palindrom or not: ")
is_palindrom(user_input)