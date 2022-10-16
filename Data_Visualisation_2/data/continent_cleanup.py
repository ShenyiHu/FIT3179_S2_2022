import csv

input_file = csv.DictReader(open('users_speed_prices.csv', 'r', encoding = 'ISO-8859-1'))
output_file = open('continent.csv', 'w')

list = []

for col in input_file:
    list.append((col['Continent'], col['Price'], col['Year']))

csv.writer(output_file).writerow(['Continent', 'Price', 'Year'])

americas_count, africa_count, asia_count, europe_count, oceania_count, americas_2020, africa_2020, asia_2020, europe_2020, oceania_2020, americas_2022, africa_2022, asia_2022, europe_2022, oceania_2022 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
for data in list:
    continent = data[0]
    price = float(data[1])
    year = int(data[2])

    if year == 2021:
        continue

    match continent:
        case "Americas":
            if year == 2020:
                americas_count += 1
                americas_2020 += price
            else:
                americas_2022 += price
        case "Africa":
            if year == 2020:
                africa_count += 1
                africa_2020 += price
            else:
                africa_2022 += price
        case "Asia":
            if year == 2020:
                asia_count += 1
                asia_2020 += price
            else:
                asia_2022 += price
        case "Europe":
            if year == 2020:
                europe_count += 1
                europe_2020 += price
            else:
                europe_2022 += price
        case "Oceania":
            if year == 2020:
                oceania_count += 1
                oceania_2020 += price
            else:
                oceania_2022 += price

americas_avg_2020 = americas_2020 / americas_count
csv.writer(output_file).writerow(["Americas", round(americas_avg_2020, 2), 2020])
americas_avg_2022 = americas_2022 / americas_count
csv.writer(output_file).writerow(["Americas", round(americas_avg_2022, 2), 2022])

africa_avg_2020 = africa_2020 / africa_count
csv.writer(output_file).writerow(["Africa", round(africa_avg_2020, 2), 2020])
africa_avg_2022 = africa_2022 / africa_count
csv.writer(output_file).writerow(["Africa", round(africa_avg_2022, 2), 2022])

asia_avg_2020 = asia_2020 / asia_count
csv.writer(output_file).writerow(["Asia", round(asia_avg_2020, 2), 2020])
asia_avg_2022 = asia_2022 / asia_count
csv.writer(output_file).writerow(["Asia", round(asia_avg_2022, 2), 2022])

europe_avg_2020 = europe_2020 / europe_count
csv.writer(output_file).writerow(["Europe", round(europe_avg_2020, 2), 2020])
europe_avg_2022 = europe_2022 / europe_count
csv.writer(output_file).writerow(["Europe", round(europe_avg_2022, 2), 2022])

oceania_avg_2020 = oceania_2020 / oceania_count
csv.writer(output_file).writerow(["Oceania", round(oceania_avg_2020, 2), 2020])
oceania_avg_2022 = oceania_2022 / oceania_count
csv.writer(output_file).writerow(["Oceania", round(oceania_avg_2022, 2), 2022])

output_file.close()