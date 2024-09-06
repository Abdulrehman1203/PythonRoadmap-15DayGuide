a = {"Jake", "John", "Eric"}
b = {"John", "Jill"}
c = a & b
print(a.intersection(b))
print("Intersection using intersection() function", b.intersection(a))
print(" Intersection using & operator :", c)

print("symmetric difference using function : ", a.symmetric_difference(b))
print("symmetric difference using ^ operator", b ^ a)

print("Difference of sets using difference() function", a.difference(b))
d = a - b
print("Difference of sets using '-' operator", d)

# typecasting list to set
myset = set(["a", "b", "c"])
print("type casting list to set ", myset)

myset1 = {"Geeks", "for", 10, 52.7, True}
print(myset1)
myset1.pop()
print("Myset after removing :", myset1)

# in frozen set you cannot add element
test = frozenset([1, 2, 3, 4])

print("frozen set : ", test)

print("A: ", a)
# Union function in sets

name = {"John", "Jill", "Eric"}
name1 = {"Ray", "kai", "speed"}
name2 = {"kazuma", "Bro", "Code"}

merger = name.union(name1)
print("Union through  union() function :", merger)
merger1 = name2 | name
print("Union through the '|' operator :", merger1)
