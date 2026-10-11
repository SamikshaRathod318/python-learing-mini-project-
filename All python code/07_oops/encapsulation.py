class Car:
    def __init__(self, brand):
        self.__brand = brand +"!" # private attribute

    def get_brand(self):   # getter method to access the private attribute
        return self.__brand


car = Car("Toyota")

print(car.get_brand())