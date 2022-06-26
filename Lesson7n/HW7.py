# functions

# Exercise 1
print('\x1b[1m \nExercise 1: Formatted text \x1b[0m')


def quote():
    print("\x1b[3m \t\"Don't compare yourself with anyone in this world...")
    print("\tif you do so, you are insulting yourself.\"")
    print("\t\t\t\t\t\t\t\t\t\t\t Bill Gates\x1b[0m")  # I know it is ugly


quote()

# Exercise 2
print('\x1b[1m \nExercise 2: Range and even numbers \x1b[0m')


def range_and_even():
    first_digit = int(input('Enter first number:'))
    second_digit = int(input('Enter second number:'))
    print(f"In a range of {first_digit} and {second_digit}, there are following even numbers:")
    even_list = []

    for i in range(first_digit, second_digit+1):
        if i % 2 == 0:
            even_list.append(i)

    print(even_list)


range_and_even()


# Exercise 3
print('\x1b[1m \nExercise 3: Square \x1b[0m')


def square():
    try:
        size = int(input("Enter size of the square (up to 25): "))
        if int(size) > 25:
            raise Exception("Size is greater than 25!")
        if int(size) <= 0:
            raise Exception("Size can't be negative or zero.")

        symbol = input("Enter one symbol which will be used to draw square: ")
        if len(symbol) != 1:
            raise Exception("Function accepts only ONE symbol.")
        filling = input("Do you want square to be filled? [Y/N]: ")
        if filling.lower() not in ('y', 'n'):
            raise Exception('You must enter only Y or N.')
        if filling.lower() == 'n':
            for i in range(size):
                for j in range(size):
                    if i == 0 or i == size - 1 or j == 0 or j == size - 1:
                        print(symbol, end="  ")
                    else:
                        print(" ", end="  ")
                print()
        else:
            for i in range(size):
                for j in range(size):
                    print(symbol, end="  ")
                print()
    except ValueError as error:
        print("Error", error)
    except Exception as error:
        print("Error: ", error)


square()

# Exercise 4
print('\x1b[1m \nExercise 4: Smallest number \x1b[0m')


def smallest_n(*kwargs):
    list_of_arguments = [*kwargs]
    smallest = min(list_of_arguments)
    print(f"The smallest number in a following range {list_of_arguments} is [{smallest}].")


smallest_n(1, 2, 3, -4, 5, -6)

# Exercise 5
print('\x1b[1m \nExercise 5: Product of numbers in a range \x1b[0m')

def product_in_range(lower_bound, higher_bound):
    list = [lower_bound, higher_bound]
    list.sort()
    product = 1
    for i in range(list[0], list[1]+1):
        product = product * i
    print(f" Prduct of numbers in a following range {list} is {product}.")

product_in_range(5, 2)


# Exercise 6
print('\x1b[1m \nExercise 6: Count digits in a number \x1b[0m')

def len_of_number(number):
    print(f"The number of digits in {number} is {len(str(number))}.")

len_of_number(10500)


# Exercise 7
print('\x1b[1m \nExercise 7: Digital palindrome test \x1b[0m')
def polindrome(integer):
    palindrome = True
    normalised_integer = str(integer)
    for i in range(0, int(len(normalised_integer) / 2)):
        if normalised_integer[i] != normalised_integer[len(normalised_integer) - i - 1]:
            palindrome = False
    if palindrome:
        print(f'{integer} is a polindrome.')
    else:
        print(f'{integer} is NOT a polindrome.')

polindrome(121)