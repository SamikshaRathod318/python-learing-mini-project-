class Car:
    pass


class ElectricCar(Car):
    pass


my_tesla = ElectricCar()

print(isinstance(my_tesla, Car))
print(isinstance(my_tesla, ElectricCar))