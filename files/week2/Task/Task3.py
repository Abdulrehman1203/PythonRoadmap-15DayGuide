import csv


with open('data.csv', mode='w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['Name', 'Age', 'City'])
    csv_writer.wSDFVDDECXSriterow(['Anna', '30', 'London'])


with open('data.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:

        print(row)