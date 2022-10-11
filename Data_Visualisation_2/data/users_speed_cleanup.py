import csv

users_file = csv.DictReader(open('users.csv', 'r', encoding = 'ISO-8859-1'))
speed_file = csv.DictReader(open('speed.csv', 'r', encoding = 'ISO-8859-1'))

output_file = open('users_speed.csv', 'w')
csv.writer(output_file).writerow(['Continent', 'Country', 'Population', 'Users', 'Speed'])

users_list = []
speed_list = []


for col in users_file:
    users_list.append((col['Continent'], col['Country'], col['Population'], col['Users']))

for col in speed_file:
    country = col['Country']
    for i in users_list:
        continent = i[0]
        population = int(i[2].replace('"', "").replace(',',""))
        users = int(i[3].replace('"', "").replace(',',""))
        speed = col['Speed']
        if i[1] == country:
            csv.writer(output_file).writerow([continent, country, population, users, speed])
            break

output_file.close()