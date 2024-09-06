import json

# Writing to a JSON file
data = {
    "Name": "Darren Watkins Jr",
    "Age": 23,
    "City": "New York"
}

with open('data.json', mode='w') as file:
    json.dump(data, file, indent=4)


# Reading a JSON file
with open('data.json', mode='r') as file:
    data = json.load(file)
    print(data)

