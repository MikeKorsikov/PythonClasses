# Python design patterns
# https://www.geeksforgeeks.org/python-design-patterns/
# UML

from abc import ABC, abstractmethod


class AbstractCar(ABC):
    @abstractmethod
    def get_body(self):
        pass


class SedanCar(AbstractCar):
    def __init__(self):
        self.body = 'Sedan'

    def __get_body(self):
        return 'Sedan'


class HatchbackCar(AbstractCar):
    def __init__(self):
        self.body = 'Hatchback'

    def __get_body(self):
        return 'Hatchback'


class PickupCar(AbstractCar):
    def __init__(self):
        self.body = 'Pickup'

    def __get_body(self):
        return 'Pickup'


class CarFactory:
    pass  # todo
