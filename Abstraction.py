from abc import ABC, abstractmethod

class Shape:
    def __init__(self):
        pass
    
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
class Circle(ABC):
    def __init__(self,r):
        self.r=r
    
    def area(self):
        return 3.14*self.r*self.r
    
    def perimeter(self):
        return 2*3.14*self.r
    
class Square(ABC):
    def __init__(self,l):
        self.l=l
        
    def area(self):
            return self.l*self.l

    def perimenter(self):
        return 4*self.l 
    
obj=Circle(5)
print(obj.area())
print(obj.perimeter())

obj1=Square(4)
print(obj1.area())
print(obj1.perimenter())       
    
        