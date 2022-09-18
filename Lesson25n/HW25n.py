print('Exercise Pizza:\n')

class Pizza1:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        print('Name: Margherita')
        print('Ingredients: basil, mozzarella, and tomato.')
        return self.func(*args)


class Pizza2:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        print('Name: Four Cheeses')
        print('Ingredients: tomato sauce, mozzarella, gorgonzola, '
              'Parmigiano Reggiano, and goat cheese.')
        return self.func(*args)


class Pizza3:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        print('Name: Capricciosa')
        print('Ingredients: mozzarella cheese, Italian baked ham, '
              'mushroom, artichoke and tomato.')
        return self.func(*args)


class Pizza4:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        print('Name: Hawaiian')
        print('Ingredients: pizza sauce, cheese, cooked ham, and pineapple.')
        return self.func(*args)


# function for ordering pizza
def orderPizza(quantity):
    print(f"{quantity} pizza ordered:")

    @Pizza3
    def bakePizza():
        print('[Pizza is baking...]')

    bakePizza()


# invoking
orderPizza(1)
