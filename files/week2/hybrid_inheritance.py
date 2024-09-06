"""Combination of two or more types of inheritance is called as Hybrid Inheritance.
 For instance, it could be a mix of single and multiple inheritance"""

class CEO:
    def ceoMethod(self):
        print("I am the CEO")


class Manager(CEO):
    def managerMethod(self):
        print("I am the Manager")


class Employee1(Manager):
    def employee1Method(self):
        print("I am Employee one")


class Employee2(Manager, CEO):
    def employee2Method(self):
        print("I am Employee two")

    # creating instances


emp = Employee2()
# method calls
emp.managerMethod()
emp.ceoMethod()
emp.employee2Method()