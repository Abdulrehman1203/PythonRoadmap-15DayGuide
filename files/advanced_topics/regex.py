import re

pattern = '^a...s$'
test_string = 'abyss'
result = re.match(pattern, test_string)

# we use '' and r' expression '  for use that as a raw string
# [] specify a set of characters i.e [abc], [a-e], [1-10] .
# for compliment  we use  ^ i.e [^abc] that means anything except abc

pattern1 = '[abc]'
test_string1 = "curse"

# Use re.search() to find the first match
result1 = re.search(pattern, test_string)

# The re.findall() method returns a list of strings containing all matches.
test_string2 = 'hello 12 hi 89. Howdy 34'
pattern2 = '\d+'

result2 = re.findall(pattern2, test_string2)

# The re.split method splits the string where there is a match and
# returns a list of strings where the splits have occurred.

test_string3 = 'Twelve:12 Eighty nine:89.'
pattern3 = '\d+'

# You can pass max split argument to the re.split() method. It's the maximum number of splits that will occur.
result3 = re.split(pattern3, test_string3)

# The method returns a string where matched occurrences are replaced with the content of replace variable.
test_string4 = 'abc 12\
de 23 \n f45 6'

# matches all whitespace characters
pattern4 = '\s+'

# empty string
replace = '-'

result4 = re.sub(pattern4, replace, test_string4)
new_string = re.subn(pattern4, replace, test_string4)





if result1:
    print("Pattern found:", result1.group())
else:
    print("Pattern not found.")

if result:
    print("Search successful.")
else:
    print("Search unsuccessful.")

print(result2)

print(result3)

print(result4)
print(new_string)

