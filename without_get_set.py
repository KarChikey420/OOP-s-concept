class Addition:
    def __init__(self,num1,num2):
        self.__num1=num1
        self.__num2=num2

    @property
    def add(self):
        return f"The Addition of two number is: {self.__num1+self.__num2}"
    
    def set_value(self,value1,value2):
        self.__num1=value1
        self.__num2=value2
        
        
obj=Addition(4,5)
print(obj.add)

obj.set_value(1,2)
print(obj.add)