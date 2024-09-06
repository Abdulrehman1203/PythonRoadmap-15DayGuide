# *args = non-keyword arguments
# **kwargs =  keywords arguments
class Car:
    # args receives unlimited no. of arguments as an array
    def __init__(self, *args):
        # access args index like array does
        self.speed = args[0]
        self.color = args[1]


class Car2:
    # args receives unlimited no. of arguments as an array
    def __init__(self, **kwargs):
        # access args index like array does
        self.speed = kwargs['s']
        self.color = kwargs['c']


def fun(a, b, c, *args):
    print("first :", a, end=" ")
    print("second :", b, end=" ")
    print("third :", c, end=" ")
    print("extra :", list(args))


def fun2(a, b, c,d, **kwargs):
    print("first :", a, end=" ")
    print("second :", b, end=" ")
    print("third :", c, end=" ")
    print("fourth :", d, end=" ")
    if kwargs.get("car") == "bmw":
        print(" Cars :", list(kwargs.values()))
    # print ("extra :", list(kwargs.items()))


fun(1, 2, 3, 4, 5, 6)
fun2(9, 8, 7, 6, car="bmw", car1="mercedes", car2="toyota", car3="ford")

# creating objects of car class
audi = Car(200, 'red')
bmw = Car(250, 'black')
mb = Car(190, 'white')

# printing the color and speed of the cars
print(audi.color)
print(bmw.speed)

# -----------------
# creating objects of car class
audi1 = Car2(s=200, c='red')
bmw1 = Car2(s=250, c='black')
mb1 = Car2(s=190, c='white')

# printing the color and speed of cars
print(audi1.color)
print(bmw1.speed)
