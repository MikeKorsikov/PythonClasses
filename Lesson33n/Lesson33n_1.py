# Abstract Factory

from abc import ABC, abstractmethod


class Body(ABC):
    @abstractmethod
    def assemble_engine(self):
        ''' engine '''

    @abstractmethod
    def set_body_type(self):
        ''' body type '''


class Hardware(ABC):
    @abstractmethod
    def put_console(self):
        ''' console '''

    @abstractmethod
    def assemble_seats(self):
        ''' sits '''


# car types
class RegularBody(Body):
    def assemble_engine(self):
        print('1.2')

    def set_body_type(self):
        print('Hatchback')


class SportBody(Body):
    def assemble_engine(self):
        print('3.2')

    def set_body_type(self):
        print('Sedan')


# hardware types
class StandardHardware(Hardware):
    def put_console(self):
        print('Normal screen')

    def assemble_seats(self):
        print('Regular seats')


class LuxuryHardware(Hardware):
    def put_console(self):
        print('Super screen')

    def assemble_seats(self):
        print('Leather seats')


# car factory
class CarFactory(ABC):
    def get_body(self) -> Body:
        ''' return body '''

    def get_hardware(self) -> Hardware:
        ''' return tangible parts '''


# car types
class FamilyCar(CarFactory):
    def get_body(self) -> Body:
        return RegularBody()

    def get_hardware(self) -> Hardware:
        return StandardHardware()


class OutdoorCar(CarFactory):
    def get_body(self) -> Body:
        return SportBody()

    def get_hardware(self) -> Hardware:
        return StandardHardware()


class BachelorCar(CarFactory):
    def get_body(self) -> Body:
        return RegularBody()

    def get_hardware(self) -> Hardware:
        return LuxuryHardware()


class WealthyCar(CarFactory):
    def get_body(self) -> Body:
        return SportBody()

    def get_hardware(self) -> Hardware:
        return LuxuryHardware()


#
def test2(model):
    factory = {
        'Family': FamilyCar(),
        'Outdoor': OutdoorCar(),
        'Bachelor': BachelorCar(),
        'Wealthy': WealthyCar()
    }

    car = factory[model]
    body = car.get_body()
    hardware = car.get_hardware()

    body.assemble_engine()
    body.set_body_type()

    hardware.put_console()
    hardware.assemble_seats()

# create instance
test2('Family')



