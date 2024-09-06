"""In multilevel inheritance, a class is derived from another derived class.
 There exists multiple layers of inheritance. We can imagine it as a grandparent-parent-child relationship."""
class Universe:
    def universeMethod(self):
        print("I am in the Universe")


# child class
class Earth(Universe):
    def earthMethod(self):
        print("I am on Earth")


# another child class
class US(Earth):
    def united_state_method(self):
        print("I am in United States")

    # creating instance


person = US()
# method calls
person.universeMethod()
person.earthMethod()
person.united_state_method()