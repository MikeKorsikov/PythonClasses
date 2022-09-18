# iteration (looping)

# Reading raw CSV file
print('\nReading raw CSV data from the file:')
import os

os.chdir('/Users/mykolakorsikov/PycharmProjects/Python/HeadFirst_Python/Chapter12')

with open('buzzers.csv') as raw_data:
    print(raw_data.read())

# Reading CSV file as list
print('\nReading CSV file as lists:')
import csv

with open('buzzers.csv') as data:
    for line in csv.reader(data):
        print(line)

# Reading CSV file as Dictionaries
print('\nReading CSV file as dictionaries:')
import csv

with open('buzzers.csv') as data:
    for line in csv.DictReader(data):
        print(line)

# Converting CSV data into single dictionary
print('\nConvert raw data into single dictionary:')
with open('buzzers.csv') as data:
    ignore = data.readline()
    flights = {}
    for line in data:
        k, v = line.strip().split(',')
        flights[k] = v
print(flights)

print('\nAfter importing pprint():')
import pprint

pprint.pprint(flights)

# Converting data
print('\nConverting 24h to AM/PM format and changing names to lower case:')
from datetime import datetime


def convert2ampm(time24: str) -> str:
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')


with open('buzzers.csv') as data:
    ignore = data.readline()
    flights = {}
    for line in data:
        k, v = line.strip().split(',')
        flights[k] = v

flights2 = {}
for k, v in flights.items():
    flights2[convert2ampm(k)] = v.title()
pprint.pprint(flights2)

#
print('\nExtracting data from dictionary to a list:')
flight_times = []
for ft in flights.keys():
    flight_times.append(convert2ampm(ft))
print(flight_times)

destinations = []
for dest in flights.values():
    destinations.append(dest.title())
print(destinations)

# COMPREHENSION (less code and faster performance)
print('\nExtracting data with Comprehension pattern:')
more_dests = [dest.title() for dest in flights.values()]
print(more_dests)

# COMPREHENSION with filtering
print('\nComprehension with filtering:')
just_freeport2 = {convert2ampm(k): v.title() for k, v in flights.items() if v == 'FREEPORT'}
print(just_freeport2)

# Turning values into keys
print('\nTransforming dictionaries:')
fts = {'09:35AM': 'Freeport',
       '09:55AM': 'West End',
       '10:45AM': 'Treasure Cay',
       '11:45AM': 'Rock Sound',
       '12:00PM': 'Treasure Cay',
       '05:00PM': 'Freeport',
       '05:55PM': 'Rock Sound',
       '07:00PM': 'West End'}

when = {}
for dest in set(fts.values()):
    when[dest] = [k for k, v in fts.items() if v == dest]

pprint.pprint(when)

# Generators
print('\nGenerators, releasing one item at a time (to avoid waiting):')

# Import required library:
import requests

# Define tuple with items:
urls = ('https://headfirstlabs.com', 'https://twitter.com', 'https://oreilly.com')

# Define generator (comprehension surrounded by parenthesis):
for resp in (requests.get(url) for url in urls):
    # Process generated data:
    print(len(resp.content), '->', resp.status_code, '->', resp.url)

# Define generator function
print('\nDefine generator functions:')


def gen_from_urls(urls: tuple) -> tuple:
    for resp in (requests.get(url) for url in urls):
        yield len(resp.content), resp.status_code, resp.url


urls_res = {url: size for size, _, url in gen_from_urls(urls)}
pprint.pprint(urls_res)
