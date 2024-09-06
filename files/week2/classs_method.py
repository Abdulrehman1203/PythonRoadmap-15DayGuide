class Car:
    # Class attribute
    num_wheels = 4

    # Constructor (Instance method)
    def __init__(self, color, model):
        self.color = color  # Instance attribute
        self.model = model  # Instance attribute

    # Instance method
    def start_engine(self):
        return f"The {self.model}'s engine is now running."

    # Class method
    @classmethod
    def change_num_wheels(cls, new_wheel_count):
        cls.num_wheels = new_wheel_count

    # Static method
    @staticmethod
    def honk_horn():
        return "Beep beep!"


my_car = Car("Red", "Toyota")

# Access instance attributest
print(my_car.color)  # Output: Red

# Call instance method
print(my_car.start_engine())  # Output: The Toyota's engine is now running.

# Call class method
Car.change_num_wheels(6)
print(Car.num_wheels)  # Output: 6
