import csv

input_file = csv.DictReader(open('users_speed_prices.csv', 'r', encoding = 'ISO-8859-1'))
output_file = open('rank.csv', 'w')

tup_list = []
for col in input_file:
    tup_list.append((col['Continent'], col['Country'], col['Population'], col['Users'], col['Speed'], col['Price'], col['Year']))

tup_list1 = []
for tup in tup_list:
    if tup[6] == "2022":
        tup_list1.append(tup)

tup_list1.sort(key=lambda tup: tup[5], reverse=True)
i = 1
tup_list2 = []
for tup in tup_list1:
    tup_list2.append(tup + (i,))
    i += 1

csv.writer(output_file).writerow(['Continent', 'Country', 'Population', 'Users', 'Speed', "Price", "Year", "Rank"])
for tup in tup_list:
    for tup1 in tup_list2:
        if tup[1] == tup1[1]:
            if tup[6] == "2022":
                tup += (tup1[7],)
            else:
                tup += ("",)
            csv.writer(output_file).writerow([tup[0], tup[1], tup[2], tup[3], tup[4], tup[5], tup[6], tup[7]])

output_file.close()