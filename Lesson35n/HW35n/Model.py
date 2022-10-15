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
    f = open('shoes_db.json', 'w')
    data = json.dumps(stock)
    f.write(data)
    f.close()


def find_stock():
    print('\n\t1) Who are you looking shoes for?'
          '\n[1] Male'
          '\n[2] Female'
          '\n[3] Any')
    gender_selected = str(input('>>> '))

    print('\n\t2) What type of shoes are you looking for?'
          '\n[1] Sneakers'
          '\n[2] Boots'
          '\n[3] Sandals'
          '\n[4] Brogues'
          '\n[5] High heels'
          '\n[6] Any')
    category_selected = str(input('>>> '))

    print('\n\t1) What color are you looking for?'
          '\n[1] Black'
          '\n[2] White'
          '\n[3] Red'
          '\n[4] Any')
    color_selected = str(input('>>> '))

    print('\n\t1) What producer are you looking for?'
          '\n[1] Adidas'
          '\n[2] Nike'
          '\n[3] Ukrainske vzuttya'
          '\n[4] Any')
    producer_selected = str(input('>>> '))

    for i in stock:
        pass

# sample of dictionary
# {
#   "0": {
#     "gender": "m",
#     "category": "boots",
#     "color": "black",
#     "price": 100,
#     "producer": "ukrainske vzuttya",
#     "size": 43
#   },
#     "1": {
#     "gender": "f",
#     "category": "sneakers",
#     "color": "red",
#     "price": 100,
#     "producer": "Nike",
#     "size": 36
#   }
# }
