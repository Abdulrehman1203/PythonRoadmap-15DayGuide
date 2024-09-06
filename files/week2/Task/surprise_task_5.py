def process_number():
    """
    Continuously prompts the user to enter an integer until a negative value is entered.

    The function checks if the input integer is between 2000 and 4700, divisible by 7, and
    not a multiple of 5. All valid numbers are collected and printed as a comma-separated string
    after the user enters a negative value to stop.

    Exceptions:
        - Raises a ValueError if the input is not a valid integer.
    """

    valid_numbers = []

    while True:
        try:
            num = int(input("Enter an integer (negative num for exiting): "))

            if num < 0:
                print("Negative value entered. Exiting.")
                break

            if 2000 <= num <= 4700 and num % 7 == 0 and num % 5 != 0:
                valid_numbers.append(str(num))

        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    if valid_numbers:
        print("Valid numbers: " + ", ".join(valid_numbers))
    else:
        print("No valid numbers were entered.")


process_number()
