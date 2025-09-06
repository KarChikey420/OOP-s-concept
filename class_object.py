class Car:                     
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        
    def description(self):
     return f"{self.brand} {self.model}"
     

car=Car("volvo","2020")
print(car.description())
    