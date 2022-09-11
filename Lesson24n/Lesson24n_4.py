class myDecorator:
    def __init__(self, fn):
        self.fn = fn

    def __call__(self, num1, num2):
        return self.fn(num1, num2) ** 2


@myDecorator
def addNums(x, y):
    return x + y


print(addNums(2, 3))
