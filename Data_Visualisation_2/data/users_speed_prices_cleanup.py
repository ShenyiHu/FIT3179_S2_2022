import csv

users_file = csv.DictReader(open('users.csv', 'r', encoding = 'ISO-8859-1'))
speed_file = csv.DictReader(open('speed.csv', 'r', encoding = 'ISO-8859-1'))
prices_file = csv.DictReader(open('prices_all.csv', 'r', encoding = 'ISO-8859-1'))

output_file = open('users_speed_prices.csv', 'w')
csv.writer(output_file).writerow(['Continent', 'Country', 'Population', 'Users', 'Speed', "Price", "Year"])

users_list = []
speed_list = []
prices_list = []

for col in users_file:
    users_list.append((col['Continent'], col['Country'], col['Population'], col['Users']))

for col in prices_file:
    prices_list.append((col['Country'], col['Price (2020)'], col['Price (2021)'], col['Price (2022)']))

for col in speed_file:
    country = col['Country']
    for i in users_list:
        for j in prices_list:
            if i[1] == country and j[0] == country:
                continent = i[0]
                population = int(i[2].replace('"', "").replace(',',""))
                users = int(i[3].replace('"', "").replace(',',""))
                speed = col['Speed']
                price_2020 = j[1]
                price_2021 = j[2]
                price_2022 = j[3]
                csv.writer(output_file).writerow([continent, country, population, users, speed, price_2020, "Jan 1 2020"])
                csv.writer(output_file).writerow([continent, country, population, users, speed, price_2021, "Jan 1 2021"])
                csv.writer(output_file).writerow([continent, country, population, users, speed, price_2022, "Jan 1 2022"])
                break

output_file.close()