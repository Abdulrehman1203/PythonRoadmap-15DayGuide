class Shape:
    def draw(self):
        raise NotImplementedError("Subclasses should implement this method")


class Drawer:

        def draw_shape(self, shape):
            try:
                shape.draw()
            except AttributeError:
                print("Object does not have a draw method")


class Circle(Shape):
    def draw(self):
        print("Drawing a circle")


class Rectangle(Shape):
    def draw(self):
        print("Drawing a rectangle")


class DrawingApp:
    def __init__(self):
        self.drawer = Drawer()

    def add_shape(self, shape):
        self.drawer.draw_shape(shape)


# Create instances of shapes
circle = Circle()
rectangle = Rectangle()

# Create an instance of the drawing application
app = DrawingApp()

# Draw shapes using the application
app.add_shape(circle)  # Output: Drawing a circle
app.add_shape(rectangle)  # Output: Drawing a rectangle

"""class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Bird:
    def speak(self):
        return "Tweet!"

def animal_sounds(animal):
    print(animal.speak())

# Using different animal objects
dog = Dog()
cat = Cat()
bird = Bird()

animal_sounds(dog)  # Woof!
animal_sounds(cat)  # Meow!
animal_sounds(bird) # Tweet!
"""