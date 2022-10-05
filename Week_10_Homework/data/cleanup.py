import csv

input_file = csv.DictReader(open('prices_old.csv', 'r', encoding = 'ISO-8859-1'))
output_file = open('prices.csv', 'w')

list = []

for col in input_file:
    list.append((col['Name'], col['Average price of 1GB (USD)']))

csv.writer(output_file).writerow(['Country', 'Price'])

for data in list:
    country = data[0]
    try:
        price = float(data[1][1:])
    except:
        continue

    csv.writer(output_file).writerow([country, price])

output_file.close()