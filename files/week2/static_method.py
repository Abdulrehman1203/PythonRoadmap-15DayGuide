class Car:
    # Class attribute
    num_wheels = 4

    # Constructor (Instance method)
    def __init__(self):
        pass

    @staticmethod
    def honk_horn():
        return "Beep beep!"


# Call static method
print(Car.honk_horn())
