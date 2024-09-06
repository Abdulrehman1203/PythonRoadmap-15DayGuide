def my_decorator(some_function):
    def wrapper(num):
        print("Inside wrapper to check odd/even")
        if num % 2 == 0:
            ret = "Even"
        else:
            ret = "Odd!"
        some_function(num)
        return ret

    print("wrapper function is called")
    return wrapper


@my_decorator
def my_function(x):
    print("The number is=", x)


no = 11
print("It is ", my_function(no))
