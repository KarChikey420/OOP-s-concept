from abc import ABC , abstractmethod

pi=3.14

class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class ractangle(Shape):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    
    def area(self):
        return f"The area of a ractangle:{self.a * self.b}"
    
    def perimeter(self):
        return f"The perimeter of a ractangle:{2*(self.a+self.b)}"
        
class circle(Shape):
    def __init__(self,r):
        self.r=r
        
    def area(self):
        return f"The area of a circle:{pi*self.r*self.r}"
        
    def perimeter(self):
        return f"The perimeter of a circle:{2*pi*self.r}"

obj=ractangle(2,3)
print(obj.area())
print(obj.perimeter())

obj1=circle(3)
print(obj1.area())
print(obj1.perimeter())
    
    
    
    