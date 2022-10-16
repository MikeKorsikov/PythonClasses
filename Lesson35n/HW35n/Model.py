# Model - manages the data and defines rules
# Only model has access to database

import json

stock = []
filters_list = ['gender', 'category', 'color', 'price', 'producer', 'size']
gender_dict = {1: 'm', 2: 'f'}
category_dict = {1: 'sneakers', 2: 'boots', 3: 'sandals', 4: 'brogues', 5: 'high heels'}
color_dict = {1: 'black', 2: 'white', 3: 'red'}
# price is subject to rules >0 and < 1000
producer_dict = {1: 'Adidas', 2: 'Nike', 3: 'Ukrainske vzuttya'}


# size is subject to rules > 10 and < 50


class Shoes:
    def __init__(self,
                 gender=None, category=None, color=None, price=None, producer=None, size=None):
        self.gender = gender
        self.category = category
        self.color = color
        self.price = price
        self.producer = producer
        self.size = size

    def __str__(self):
        return f"{self.gender} - " \
               f"{self.category} - " \
               f"{self.color} - " \
               f"{self.price} - " \
               f"{self.producer} - " \
               f"{self.size}."


def retrieve_data():
    f = open('shoes_db.json')
    data = list(json.loads(f.read()).values())
    f.close()
    for SKU in data:
        stock.append(Shoes(SKU['gender'],
                           SKU['category'],
                           SKU['color'],
                           SKU['price'],
                           SKU['producer'],
                           SKU['size']))
    return stock


def save_data():
    stock_list_of_dict = []
    stock_dict_of_dict = {}
    count = 0

    for obj in stock:
        dictSKU = obj.__dict__
        stock_list_of_dict.append(dictSKU)

    for dictionary in stock_list_of_dict:
        count += 1
        record = {count: dictionary}
        stock_dict_of_dict.update(record)

    f = open('shoes_db.json', 'w')
    json_stock = json.dumps(stock_dict_of_dict)
    f.write(json_stock)
    f.close()


def find_stock():
    print('\n\t1) Who are you looking shoes for?'
          '\n[1] Male'
          '\n[2] Female'
          '\n[3] Any')
    gender_selected = int(input('>>> '))

    print('\n\t2) What type of shoes are you looking for?'
          '\n[1] Sneakers'
          '\n[2] Boots'
          '\n[3] Sandals'
          '\n[4] Brogues'
          '\n[5] High heels'
          '\n[6] Any')
    category_selected = int(input('>>> '))

    print('\n\t3) What color are you looking for?'
          '\n[1] Black'
          '\n[2] White'
          '\n[3] Red'
          '\n[4] Any')
    color_selected = int(input('>>> '))

    print('\n\t4) What producer are you looking for?'
          '\n[1] Adidas'
          '\n[2] Nike'
          '\n[3] Ukrainske vzuttya'
          '\n[4] Any')
    producer_selected = int(input('>>> '))

    for i in stock:
        pass


def add_stock():
    print('\n\t1) Are these shoes for women or men?'
          '\n[1] Male'
          '\n[2] Female')
    selection = int(input('>>> '))
    gender_assigned = (gender_dict[selection])
    print(gender_assigned)

    print('\n\t2) Type of shoes?'
          '\n[1] Sneakers'
          '\n[2] Boots'
          '\n[3] Sandals'
          '\n[4] Brogues'
          '\n[5] High heels')
    selection = int(input('>>> '))
    category_assigned = (category_dict[selection])
    print(category_assigned)

    print('\n\t3) Color?'
          '\n[1] Black'
          '\n[2] White'
          '\n[3] Red')
    selection = int(input('>>> '))
    color_assigned = (color_dict[selection])
    print(color_assigned)

    print('\n\t4) Price?')
    price_assigned = round(float(input('>>> ')), 2)

    print('\n\t5) Manufacturer?'
          '\n[1] Adidas'
          '\n[2] Nike'
          '\n[3] Ukrainske vzuttya')
    selection = int(input('>>> '))
    producer_assigned = (producer_dict[selection])
    print(producer_assigned)

    print('\n\t6) Shoe size?')
    size_assigned = int(input('>>> '))

    SKU_object = Shoes(gender_assigned,
                       category_assigned,
                       color_assigned,
                       price_assigned,
                       producer_assigned,
                       size_assigned)

    stock.append(SKU_object)
    save_data()


def go_on():
    print('\nDo you want to continue? [Y/N]')
    selection = str(input('>>>')).lower()
    if selection == 'n':
        print('\n\tSession terminated.')
        exit()
    else:
        pass
