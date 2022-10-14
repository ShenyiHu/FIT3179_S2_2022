import csv

input_file = csv.DictReader(open('prices_old.csv', 'r', encoding = 'ISO-8859-1'))
output_file = open('prices_all.csv', 'w')

list = []

for col in input_file:
    list.append((col['Name'], col['Average price of 1GB (USD - at the start of 2020)'], col['Average price of 1GB (USD - at the start of 2021)'], col['Average price of 1GB (USD)'], col['Cheapest 1GB for 30 days (USD)'], col['Most expensive 1GB (USD)']))

csv.writer(output_file).writerow(['Country', 'Price (2020)', 'Price (2021)', 'Price (2022)', 'Cheap', 'Expensive'])

for data in list:
    country = data[0]
    try:
        price_2020 = float(data[1][1:])
        price_2021 = float(data[2][1:])
        price_2022 = float(data[3][1:])
        price_cheap = float(data[4][1:])
        price_expensive = float(data[5][1:])
    except:
        continue

    csv.writer(output_file).writerow([country, price_2020, price_2021, price_2022, price_cheap, price_expensive])

output_file.close()