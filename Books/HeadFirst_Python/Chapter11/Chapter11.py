# Exception handling
import sys

print('Example 1: File not found error:')
try:
    with open('myfiles.txt') as fh:
        file_data = fh.read()
    print(file_data)
except FileNotFoundError:
    print('The data file is missing.')
except PermissionError:
    print('This is not allowed')
except Exception as err:
    print('Some other error occurred.', str(err))

# Getting data about error
print('\nExample 2: Division by zero:')
try:
    a = 1 / 0
except:
    err = sys.exc_info()
    for e in err:
        print(e)


# creating custom exceptions

class ConnectionError(Exception):
    pass


try:
    raise ConnectionError('Whoops!')
except ConnectionError as err:
    print('Got:', str(err))
