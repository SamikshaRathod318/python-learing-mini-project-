class Battery:
    def battery_info(self):
        print("Battery: 85 kWh")


class Engine:
    def engine_info(self):
        print("Engine: Electric")


class ElectricCar(Battery, Engine):
    pass   


my_tesla = ElectricCar()

my_tesla.battery_info()
my_tesla.engine_info()