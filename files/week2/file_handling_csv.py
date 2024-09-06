import csv

"""
Data writing in CSV file
"""
with open('data.csv', mode='w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['Name', 'Age', 'City'])
    csv_writer.writerow(['Anna', '30', 'London'])

"""
Data Appending in CSV file
"""
with open('data.csv', mode='a', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['Mark', '28', 'Paris'])

"""
Data reading in CSV file
"""
with open('data.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:

        print(row)

# Writing CSV as a dictionary

with open('data.csv', mode='a', newline='') as file:
    fieldnames = ['Name', 'Age', 'City']
    csv_writer = csv.DictWriter(file, fieldnames=fieldnames)

    csv_writer.writeheader()
    csv_writer.writerow({'Name': 'Henry', 'Age': '28', 'City': 'New York'})
    csv_writer.writerow({'Name': 'Darren Watkins Jr', 'Age': '19', 'City': 'Ohio'})

# Reading CSV as a dictionary
with open('data.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row)
