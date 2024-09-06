
def frequency_calculator(a):
    for i in a:
        f = a.count(i)
        print(f"Frequency of {i} in string is : {f}")


a = input("Enter a string :")

frequency_calculator(a)

