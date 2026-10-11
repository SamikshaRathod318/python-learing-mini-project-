class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.__model = model

    @property
    def model(self):
        return self.__model


car = Car("Tesla", "Model S")

print(car.model)