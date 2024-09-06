class Student:

    def __init__(self, name="Umer", marks=82):
        self.__name = name
        self.__marks = marks

    def studentdata(self):
        print("Name: {} marks: {}".format(self.__name, self.__marks))


s1 = Student()
s2 = Student("BroCode", 25)

s1.studentdata()
s2.studentdata()
#print("Name: {} marks: {}".format(s1._Student__name, s2.__marks))
print("Name: {} marks: {}".format(s2._Student__name, s2._Student__marks))
