print('Exercise - Fraction Class:\n')


class Fraction:
    def __init__(self, numerator=0, denominator=0):
        self.numerator = numerator
        self.denominator = denominator

    # returning fraction x/y without being called
    def __str__(self):
        return str(self.numerator) + '/' + str(self.denominator)

    def show_fraction(self):
        print(f'{self.numerator}/{self.denominator}')

    def get_numerator(self):
        return self.numerator

    def set_numerator(self, new_numerator):
        self.numerator = new_numerator
        return new_numerator

    def get_denominator(self):
        return self.denominator

    def set_denominator(self, new_denominator):
        self.denominator = new_denominator
        return new_denominator

    def add_fractions(self, fraction2):
        result_numerator = self.numerator * fraction2.denominator + self.denominator * fraction2.numerator
        result_denominator = self.denominator * fraction2.denominator
        result = f'{result_numerator}/{result_denominator}'
        return result

    def multiply_fractions(self, fraction2):
        result_numerator = self.numerator * fraction2.numerator
        result_denominator = self.denominator * fraction2.denominator
        result = f'{result_numerator}/{result_denominator}'
        return result


# create first object
example1 = Fraction(1, 2)

# display fraction with __str__
print('Showing fraction via return:')
print(example1)

# calling function to display fraction
print('\nCalling function to display fraction:')
example1.show_fraction()

# getting numerator
print('\nGetting numerator:')
print('Numerator is:', example1.get_numerator())

# getting denominator
print('\nGetting denominator:')
print('Denominator is:', example1.get_denominator())

# setting numerator
print('\nSetting numerator:')
print('New numerator is:', example1.set_numerator(5))

print('\nFraction with new numerator:')
example1.show_fraction()

# setting denominator
print('\nSetting denominator:')
print('New denominator is:', example1.set_denominator(2))

print('\nFraction with new denominator:')
example1.show_fraction()

# create second object
print('\nCreate second object:')
example2 = Fraction(1, 3)
example2.show_fraction()
print('Numerator is:', example2.get_numerator())
print('Denominator is:', example2.get_denominator())

# testing addition
print('\nTesting addition of functions:')
print(f'{example1} + {example2} =')
example3 = Fraction.add_fractions(example1, example2)
print(example3)

# testing addition
print('\nTesting multiplication of functions:')
example4 = Fraction(5, 7)
example5 = Fraction(1, 15)
print(f'{example4} * {example5} =')
example6 = Fraction.multiply_fractions(example4, example5)
print(example6)

# getting parameters from object
print(example5.numerator)
print(example5.denominator)
