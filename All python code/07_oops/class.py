class Car:                                         #creating a class
    def __init__(self, brand, model):   #create a constructor  __init__ is a constructor that is called when an object is created

        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"

my_car = Car("Toyota", "Camry")
print(my_car.brand)
print(my_car.model)
print(my_car.full_name())

my_new_car = Car("Honda", "Civic")
print(my_new_car.brand)
print(my_new_car.model)