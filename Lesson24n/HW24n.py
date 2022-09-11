import time

print('Exercise 1 Processing time to compute prime numbers in a defined range:')


# decorator to calculate processing time
class Timer:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        start = time.process_time()
        self.func()
        end = time.process_time()
        process_time = round(end - start, 5)
        return print(f'\nProcessing time is {process_time} sec.')


@Timer
def simple_num():  # function we want to measure
    MIN = 0
    MAX = 1000
    prime_list = []

    for number in range(MIN, MAX + 1):
        if number > 1:
            for i in range(2, number):
                if (number % i) == 0:
                    break
                else:
                    prime_list.append(number)
    prime_set = set(prime_list)
    return print(f'\n {prime_set}')


# invoking function
simple_num()


# calculating processing time using function (for validation of results)
print('\nValidation of results using function:')
def timer():
    start = time.process_time()
    print(simple_num())
    end = time.process_time()
    process_time = round(end - start, 5)
    result = f'Processing time is {process_time} sec.'
    return result


# invoking function
print(timer())

print('\nExercise 2 Processing time to compute prime numbers in a given range:')

@Timer
def simple_num2():
    START = int(input('Enter starting point: '))
    END = int(input('Enter ending point: '))
    prime_list = []

    for number in range(START, END + 1):
        if number > 1:
            for i in range(2, number):
                if (number % i) == 0:
                    break
                else:
                    prime_list.append(number)
    prime_set = set(prime_list)
    return print(prime_set)


# invoking function
simple_num2()


print('\nExercise 3 Using decorators to modify reports:')


# decorator for Tax office (excluding employees)
class taxOfficeDecorator:
    def __init__(self, function):
        self.function = function

    def __call__(self, arg1, arg2, arg3):
        print("\n\tTax Office Report:")
        result = self.function(arg1, arg2, 'NA')
        tax = f"\nTax due: {arg2 * 0.2}"
        print(result, tax)

# decorator for Shareholders (including employees)
class shareholders:
    def __init__(self, function):
        self.function = function

    def __call__(self, arg1, arg2, arg3):
        print("\n\tAnnual Report:")
        return self.function(f'{int(arg1/1000)}k', f'{int(arg2/1000)}k', f'{int(arg3)} people')


# Using first decorator
@taxOfficeDecorator
def financialReport(revenue, profit, employees):
    report = f"Revenue: {revenue}" \
             f"\nProfit: {profit}" \
             f"\nNumber of employees: {employees}."
    return report


# using second decorator
@shareholders
def financialReport(revenue, profit, employees):
    report = f"Revenue: {revenue}" \
             f"\nProfit: {profit}" \
             f"\nNumber of employees: {employees}."
    return report


print(financialReport(10_000, 2_000, 20))

