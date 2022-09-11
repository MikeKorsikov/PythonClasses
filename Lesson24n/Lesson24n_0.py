# classes part-4

# Functor

class Counter:
    def __init__(self):
        self.__i = 0

    def __call__(self, *args, **kwargs):
        print(f'calling Call functor, i: {self.__i}')
        self.__i +=1
        return self.__i

c = Counter()

c()
c()
c()

#
print('\nUsing class as function:')
class RemoveChar:
    def __init__(self, chars):
        self.__chars = chars

    def __call__(self, *args, **kwargs):
        line = args[0]
        if not isinstance(line, str):
            raise ValueError('Error message')

        return line.strip(self.__chars)

rc1 = RemoveChar("!@#$%^& ")

print(rc1("%Hello World$"))

#
print('\nUsing function:')
def RemoveChar(symbs):
    def removeChar(line):
        if not isinstance(line, str):
            raise ValueError('Error message')
        return line.strip(symbs)
    return removeChar

s1 = RemoveChar("!@#$%^& ")
print(s1("$Hello World%"))

#
print('\nWallet example:')
class WalletFunction:
    def __init__(self, startCoins):
        self.__startCoins = startCoins

    def __call__(self, coins=0):
        self.__startCoins += coins
        return self.__startCoins

userWallet = WalletFunction(100)
print(f'User starts with {userWallet()} coins.')
print(f'Added 50 so user has {userWallet(50)} coins.')
print(f'Added extra 50 so user has {userWallet(50)} coins.')