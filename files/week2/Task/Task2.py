class Vehicle:
    def __init__(self, make, model, year,no_wheels):
        self.make = make
        self.model = model
        self.year = year
        self.no_wheels = no_wheels

    def drive(self):
        print(f"Driving { self.make } { self.model}  { self.year}")

    def stop(self):
        print(f"Stopping { self.make } { self.model}  { self.year}")

class Car(Vehicle):
    def __init__(self, make, model, year, no_wheels, engine_type):
        super().__init__(make, model, year, no_wheels)
        self.engine_type = engine_type

    def display(self):
        print(f"it's a { self.make } { self.model}  { self.year} Car, with {self.engine_type} engine")


class Truck(Car):
    def __init__(self, make, model, year, no_wheels, engine_type,load_capacity):
        super().__init__(make, model, year, no_wheels, engine_type)
        self.load_capacity = load_capacity

    def display(self):
        print(f"it's a { self.make } { self.model}  { self.year} Truck with {self.engine_type} engine and {self.load_capacity}ton load capacity")



obj = Vehicle("Ford","Raptor","2019",6)
obj.drive()
obj.stop()

obj1 = Car("Mercedes","S2000",2022,4,"V12 Twin Turbo")
obj1.display()
obj1.stop()



