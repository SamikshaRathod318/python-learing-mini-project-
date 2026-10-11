class Car:
    total_cars = 0

    def __init__(self, brand):
        self.brand = brand
        Car.total_cars += 1


car1 = Car("Tata")
car2 = Car("Tesla")
car3 = Car("BMW")

print("Total cars:", Car.total_cars)