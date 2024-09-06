def is_palindrom(user_input):
    temp = user_input[::-1]

    validator = False

    if user_input == "" or user_input == " ":
        print("It's an empty string")

    elif temp == user_input:
        print("This input is a palindrome")
        validator = True
    else:
        print("Not a palindrome")


    for i in user_input:
         if "o" in user_input:
             user_input = user_input.replace("o", "")
         if "e" in user_input:
             user_input = user_input.replace("e", "")
         if "i" in user_input:
             user_input = user_input.replace("i", "")
         if "u" in user_input:
             user_input = user_input.replace("u", "")
         if "a" in user_input:
             user_input = user_input.replace("a", "")

        print("String after vowel removal:", user_input)


user_input = input("Enter a string to check whether it is a palindrome or not: ")
is_palindrom(user_input)
