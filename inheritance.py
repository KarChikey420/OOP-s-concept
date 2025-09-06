class Car:
    def __init__(self,name,brand):
        self.name=name
        self.__brand=brand
        
    def print_car(self):
        return f"{self.name} {self.__brand}"
        
class battery(Car):
    def __init__(self,name,brand,battery):
        super().__init__(name,brand)
        self.battery=battery
        
    def print_battery_car(self):
        return f"{super().print_car()} {self.battery}"
        

car1=battery("Toyota","2020","yes")
print(car1.print_battery_car())
        