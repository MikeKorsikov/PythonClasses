# decorators

class Counter:
    def __init__(self, func):
        self.func = func
        self.i = 0

    def __call__(self, *args, **kwargs):
        self.i += 1
        print(f"Function {self.func.__name__} was called {self.i} time(s).")
        return self.func(*args, **kwargs)

@Counter
def info(name):
    print(f"Hello {name}")

info('Alex')
info('Mykola')

#
class Repeater:
    def __init__(self, n):
        self.n = n

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            for i in range(self.n):
                func(*args, **kwargs)
        return wrapper


@Repeater(5)
def info():
    print('My name is Mykola')


info()

#
