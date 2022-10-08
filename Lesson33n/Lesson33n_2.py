# example of use of abstract classes

from enum import Enum


class PizzaType(Enum):
    margarita = 0,
    mexico = 1,
    stella = 2,
    dibalo = 3


class Pizza:
    def __init__(self, price):
        self.price = price

    def get_price(self):
        return self.price


class PizzaMargarita(Pizza):
    def __init__(self):
        super().__init__(20)


class PizzaMexico(Pizza):
    def __init__(self):
        super().__init__(15)


class PizzaStella(Pizza):
    def __init__(self):
        super().__init__(17)


class PizzaDiablo(Pizza):
    def __init__(self):
        super().__init__(30)


def create_pizza(type: PizzaType) -> Pizza:
    factory = {
        PizzaType.margarita: PizzaMargarita,
        PizzaType.mexico: PizzaMexico,
        PizzaType.stella: PizzaStella,
        PizzaType.dibalo: PizzaDiablo,
    }

    return factory[type]()


for pizza in PizzaType:
    my_pizza = create_pizza(pizza)
    print(f"Pizza type: {pizza} and price {my_pizza.get_price()}")
