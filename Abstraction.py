from abc import ABC,abstractmethod

class Shape(ABC):
    
    @abstractmethod
    
    def area(self):
        pass
    
    @abstractmethod
    
    def perimeter(self):
        pass
    
class Circle(Shape):
    def __init__(self,r):
        self.r=r   
    
    def area(self):
        return 3.14 * self.r * self.r
    
    def perimeter(self):
        return 2 * 3.14 * self.r
        
class ractangle(Shape):
    def __init__(self,lenght,width):
        self.lenght=lenght
        self.width=width
        
    def area(self):
        return self.lenght * self.width
        
    def perimeter(self):
        return 2 * ( self.lenght + self.width)
        
obj1=Circle(4)
obj2=ractangle(2,3)

print(f"The area of Circle:{obj1.area()}")
print(f"The perimeter of Circle:{obj1.perimeter()}")

print(f"The area of ractangle:{obj2.area()}")
print(f"The peramiter of ractangle:{obj2.perimeter()}")
