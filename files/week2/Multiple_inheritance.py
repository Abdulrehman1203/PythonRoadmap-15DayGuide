"""Multiple inheritance in Python allows you to construct a class based on more than one parent classes.
The Child class thus inherits the attributes and method from all parents.
 The child can override methods inherited from any paren"""

class division:
    def __init__(self, a, b):
        self.n = a
        self.d = b

    def divide(self):
        return self.n / self.d


class modulus:
    def __init__(self, a, b):
        self.n = a
        self.d = b

    def mod_divide(self):
        return self.n % self.d


class div_mod(division, modulus):
    def __init__(self, a, b):
        self.n = a
        self.d = b

    def div_and_mod(self):
        divval = division.divide(self)
        modval = modulus.mod_divide(self)
        return (divval, modval)


x=div_mod(10,3)
print ("division:",x.divide())
print ("mod_division:",x.mod_divide())
print ("divmod:",x.div_and_mod())