class Shape:
    def __init__(self,num1,num2):
        self.__num1=num1
        self.__num2=num2
        
    def get_number(self):  #getter method(which access the private attributes)
        return self.__num1+self.__num2
        
    def set_number(self,num1,num2):#setter method(which modify the private attributes)
        self.__num1=num1
        self.__num2=num2
        
class Squre(Shape):
    def __init__(self,side):
        
        super().__init__(side,side)
        
obj1=Squre(5)

print(obj1.get_number())

obj1.set_number(7,7)
print(obj1.get_number())

       