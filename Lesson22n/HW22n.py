print('Exercise 1, Class Car:')


class Car:
    def __init__(self, model, year, manufacturer, engine_capacity, color, price):
        # private attributes
        self.__model = model
        self.__year = year
        self.__manufacturer = manufacturer
        self.__engine_capacity = engine_capacity
        self.__color = color
        self.__price = price

    # public
    def get_info(self):
        details = f"Full info: {self.__model} - {self.__year} - {self.__manufacturer} " \
                  f"- {self.__engine_capacity} - {self.__color} - Price is NA"
        return details

    # methods setting the attributes
    def set_model(self, model):
        self.__model = model

    def set_year(self, year):
        self.__year = year

    # methods accessing specific attributes
    def get_price(self):
        price_details = f"Car price is: {self.__price}"
        return price_details

    def get_year(self):
        return self.__year


# TESTING
# create object
example1 = Car('Elegance', '1998', 'Mercedes', '2.4', 'green', '10000')

# displaying attributes via method
print(example1.get_info())

# setting attribute via method
example1.set_model('Gelendvagen')
print(example1.get_info())

# trying to access private parameter directly
try:
    print(example1.__year)
except Exception as e:
    print('\nError:', str(e))

# displaying private attribute using method
print(example1.get_price())

print('\nExercise 2, Class Book:')


class Book:
    def __init__(self, title, year, publisher, genre, author, price):
        # public attributes
        self.title = title
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        # private attributes
        self.__price = price

    # public
    def show_info(self):
        details = f"Full info: {self.title} - {self.year} - {self.publisher} " \
                  f"- {self.genre} - {self.author} - Price is NA"
        return details

    # methods setting the attributes
    def set_title(self, title):
        self.title = title

    def set_publisher(self, publisher):
        self.publisher = publisher

    # methods accessing specific attributes
    def get_price(self):
        price_details = f"Book's price is: {self.__price}"
        return price_details

    def get_author(self):
        return self.author


# TESTING
# create object
example2 = Book('Python', 2018, 'HeadFirst', 'educational', 'various', '$70')

# displaying attributes via method
print(example2.show_info())

# setting attribute via method
example2.set_title('Cryptography for Dummies')
print(example2.show_info())

# trying to access private parameter directly
try:
    print(example2.__price)
except Exception as e:
    print('\nError:', str(e))

# displaying public attribute using method
print('Author is:', example2.get_author())


print('\nExercise 3, Class Stadium:')


class Stadium:
    def __init__(self, name, opening_date, country, city, capacity):
        self.a = name
        self.b = opening_date
        self.c = country
        self.d = city
        self.e = capacity

    # public
    def info(self):
        details = f"Full details: {self.a} - {self.b} - {self.c} - {self.d} - {self.e}."
        return details

    # methods setting the attributes
    def set_name(self, name):
        self.a = name

    def set_opening_date(self, date):
        self.b = date

    # methods accessing specific attributes
    def get_capacity(self):
        details = f"Capacity of the stadium is: {self.e}"
        return details

    def get_opening_date(self):
        return self.b


# TESTING
# create object
example3 = Stadium('Millennium Dome', '01.01.2005', 'UK', 'London', 10_000)

# displaying attributes via method
print(example3.info())

# setting attribute via method
example3.set_name('Kyiv Dinamo')
print(example3.info())

# displaying public attribute using method
print(example3.get_capacity())