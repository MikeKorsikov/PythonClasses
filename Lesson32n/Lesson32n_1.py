# packing and unpacking arguments in Python (part 2)
# csv - comma-separated values
# https://www.geeksforgeeks.org/working-csv-files-python/

import csv


# record data into csv file
data = {'Sanctions_first_wave': ['Putin', 'Medvedev'],
        'Sanctions_second_wave': ['Volodin', 'Shoygu']}

try:
    file = open('data.csv', 'w')
    writer = csv.writer(file)
    writer.writerow(['Waves:', 'First_person:', 'Second_person:'])
    for key, items in data.items():
        writer.writerow([key, *items])
    writer.writerow(['END'] * 3)

    file.close()

except Exception as e:
    print(str(e))

# load data from csv file
rows = []

try:
    file = open('data.csv', 'r')
    reader = csv.reader(file)
    rows = list(reader)
    file.close()

except Exception as e:
    print(str(e))

print(rows)


#
data2 = {'Sanctions_third_wave': ['Matvienko', 'Skobeeva'],
         'Sanctions_fourth_wave': ['Kadyrov', 'Tereshkova']}

try:
    file2 = open('data2.csv', 'w')
    writer = csv.DictWriter(file2, fieldnames=['Wave', 'First_person', 'Second_person'])
    writer.writeheader()
    for key, items in data2.items():
        writer.writerow(dict(Wave=key, First_person=items[0], Second_person=items[1]))

    file2.close()

except Exception as e:
    print(str(e))

# load data from csv file
rows2 = []

try:
    file2 = open('data2.csv', 'r')
    reader = csv.DictReader(file2)
    rows2 = list(reader)
    file2.close()

except Exception as e:
    print(str(e))

print(rows2)

