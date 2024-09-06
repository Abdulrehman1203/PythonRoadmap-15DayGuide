
year = int(input("Enter a year to check if it's a leap year or not: "))

if year % 400 == 0 and year % 100 == 0:
    print(f"{year} is a leap year")
elif year % 4 == 0 and year % 100 != 0:
    print(f"{year} is a leap year")
else:
    print("Not Leap Year")

