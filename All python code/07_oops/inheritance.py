class Car:                                         #creating a class
    def __init__(self, brand, model):   #create a constructor  __init__ is a constructor that is called when an object is created

        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"

class ElectricCar(Car):  #creating a subclass of Car  also known as inheritance
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
print(my_tesla.model)
print(my_tesla.full_name())