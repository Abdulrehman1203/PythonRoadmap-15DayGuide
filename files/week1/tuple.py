
student = ("umer", 21, "male", "CS")


print(student.count("male"))
print(student.index("male"))

for i in student:
    print(i)
    print(type(i))

if "umer" in student:

    print("umer is here")

list1 = [1, 2, 3]
t = tuple(list1)
print(t)
s = {"umer", "abdullah", "shayan"}
d1 = {1: 2, 2: 3, 3: 4}
d = {1: s}

print(d)
