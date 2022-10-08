# Factory method


from abc import ABC, abstractmethod


class AbstractCar(ABC):
    @abstractmethod
    def get_body(self):
        ''' defined in each separate class '''


class SedanCar(AbstractCar):
    def __init__(self):
        self.body = 'Sedan'

    def get_body(self):
        return 'Sedan'


class HatchbackCar(AbstractCar):
    def __init__(self):
        self.body = 'Hatchback'

    def get_body(self):
        return 'Hatchback'


class PickupCar(AbstractCar):
    def __init__(self):
        self.body = 'Pickup'

    def get_body(self):
        return 'Pickup'


class CarFactory:
    @staticmethod
    def get_car(model):
        try:
            if model == "Sedan":
                return SedanCar()
            elif model == "Hatchback":
                return HatchbackCar()
            elif model == "Pickup":
                return PickupCar()
            raise AssertionError('Model not found.')
        except AssertionError as er:
            print(str(er))


# not possible to create abstract car object
# car = AbstractCar()
# print(car)

#
ls = ['Sedan', 'Hatchback', 'Pickup', 'Cabriolet']
for i in ls:
    car = CarFactory.get_car(i)
    try:
        body = car.get_body()
        print(body)
    except AttributeError as e:
        print(str(e))

