# currying functions in Python
# simplifying the execution of a function that takes multiple arguments into
# executing sequential single-argument functions

def sendMsg(userTo):
    def setMsg(msgTxt):
        def setUserFrom(userFrom):
            def setLang(lang):
                print(f'Dear {userTo},'
                      f'Hello from {userFrom},'
                      f'Welcome to {lang} world!{msgTxt} ')

            return setLang

        return setUserFrom

    return setMsg


case1 = sendMsg('admin')('Good luck!')
case2 = sendMsg('studen')('See you!')('admin')
case1('teacher')('Python')
case2('C++')


# Decorators and wrappers in Python
print('\nDecorators:\n')


def wrapper(status):
    def simpleDecorator(myFunction):
        print("Hello! I'm Decorator!")

        def simpleWrapper(*args, **kwargs):
            print(f"Profile status {status}.")
            myFunction(*args, **kwargs)
        return simpleWrapper
    return simpleDecorator


def sayHi():
    print("Welcome!")


@wrapper(status='active')
def sayHi(name):
    print(f"Welcome {name}!")


sayHi('Alex')
