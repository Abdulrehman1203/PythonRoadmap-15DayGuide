class CustomError(Exception):
    """Base class for other exceptions"""
    pass


class ValueTooSmallError(CustomError):
    """Raised when the input value is too small"""

    def __init__(self, message="Value is too small"):
        self.message = message
        super().__init__(self.message)


class ValueTooLargeError(CustomError):
    """Raised when the input value is too large"""

    def __init__(self, message="Value is too large"):
        self.message = message
        super().__init__(self.message)


class InvalidInputError(Exception):
    """Exception raised for errors in the input."""

    def __init__(self, value, message="Invalid input provided"):
        self.value = value
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.value} -> {self.message}'


def check_value(value):
    if value < 10:
        raise ValueTooSmallError(f"The value {value} is too small!")
    elif value > 100:
        raise ValueTooLargeError(f"The value {value} is too large!")
    else:
        print(f"The value {value} is within the allowed range.")


def validate_input(user_input):
    if not isinstance(user_input, int):
        raise InvalidInputError(user_input)
    print(f"Input {user_input} is valid.")


# Example usage
try:
    check_value(5)
except ValueTooSmallError as e:
    print(e)

try:
    validate_input("xyz")
except InvalidInputError as e:
    print(e)
