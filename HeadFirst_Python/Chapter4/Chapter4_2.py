# MODULES

def double(arg):
    print('Before: ', arg)
    arg = arg * 2
    print('After: ', arg)


num = 10
print(double(num))


def change(arg):
    print('Before: ', arg)
    arg.append('More data')
    print('After: ', arg)


numbers = [42, 256, 16]
print(change(numbers))
