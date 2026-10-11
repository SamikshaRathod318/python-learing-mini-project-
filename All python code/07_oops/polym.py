class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def fuel_type(self):
        return "Petrol or Diesel"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"


my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
safari = Car("Tata", "Safari")

print(my_tesla.brand, my_tesla.model, my_tesla.battery_size)
print(my_tesla.fuel_type())

print(safari.brand, safari.model)
print(safari.fuel_type())