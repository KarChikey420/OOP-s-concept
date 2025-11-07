class Car:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
        
    def display_details(self):
       return f"My car brand is {self.brand},model is {self.model} and price is {self.price}"

if __name__=="__main__":
    obj=Car("Kia","Sonet",2000000)
    print(obj.display_details())