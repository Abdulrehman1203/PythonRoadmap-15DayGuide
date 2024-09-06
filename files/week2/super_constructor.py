class ClassA:
    def __init__(self, a):
        print("ClassA initialized with", a)


class ClassB:
    def __init__(self, b,a,d):
        print("ClassB initialized with", b)


class ClassC(ClassB, ClassA):
    def __init__(self, a, b):
        super().__init__(b, a)
        ClassA.__init__(self, a)
        print("ClassC initialized")


c = ClassC(2, 3)
