from classtools import AttrDisplay


class Employee:  # General superclass
    def computeSalary(self):
        pass

    def giveRaise(self):
        pass

    def promote(self):
        pass

    def retire(self):
        pass


class Engineer(Employee):
    def computeSalary(self):
        pass


# create object
bob = Employee()
tom = Engineer()


class FirstClass:
    def setdata(self, value):
        self.data = value

    def display(self):
        print(self.data)


# x = FirstClass()
# y = FirstClass()
#
# x.setdata('King')
# y.setdata(3.14)
# x.display()
# y.display()


class Person (AttrDisplay):
    def __init__(self, name, job=None, pay=0):  # Constructor takes three arguments
        self.name = name  # Fill out fields when created
        self.job = job  # self is the new instance object
        self.pay = pay

    def lastName(self):  # Behavior methods
        return self.name.split()[-1]  # self is implied subject

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))  # Must change here only

    # def __repr__(self):
    #     return '[Person: %s, %s]' % (self.name, self.pay)


class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)  # Embed a Person object

    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent + bonus)  # Intercept and delegate

    # def __getattr__(self, attr):
    #     return getattr(self.person, attr)  # Delegate all other attrs
    #
    # def __repr__(self):
    #     return str(self.person)  # Must overload again (in 3.X)


class Department:
    def __init__(self, *args):
        self.members = list(args)

    def addMember(self, person):
        self.members.append(person)

    def giveRaises(self, percent):
        for person in self.members:
            person.giveRaise(percent)

    def showAll(self):
        for person in self.members:
            print(person)


# TESTING
if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.10)
    print(sue)
    tom = Manager('Tom Jones', 50000)
    tom.giveRaise(.10)
    print(tom.lastName())
    print(tom)

    # accessing values of the object using __dict__
    for key in bob.__dict__:
        print(key, '=>', bob.__dict__[key])

    # accessing values of the object, using getattr()
    for key in bob.__dict__:
        print(key, '=>', getattr(bob, key))

    # accessing object keys
    print(list(bob.__dict__.keys()))

    # accessing object attr, inherited attr and methods
    print(list(dir(bob)))

    # excluding magic methods
    print(list(name for name in dir(bob) if not name.startswith('__')))