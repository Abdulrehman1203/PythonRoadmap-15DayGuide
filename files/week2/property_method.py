class MyClass:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

    @value.deleter
    def value(self):
        print("Deleting value...")
        del self._value

obj = MyClass(10)
print(obj.value)  # Prints 10
del obj.value  # Calls the deleter
