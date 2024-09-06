def count_frequency(string):
    frequency={}
    for char in string:
        if char in frequency:
            frequency[char]+=1
        else:
            frequency[char]=1
    return frequency
string=input("enter the string::")
fre=count_frequency(string)
print(fre)