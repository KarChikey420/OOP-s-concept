class Shape:
    def __init__(self,num1,num2):
        self._num1=num1
        self._num2=num2
        
        
class square(Shape):
    # def __init__(self,num1,num2):
    #     super().__init__(num1,num2)
    
    def value(self):
        return self._num1+self._num2


obj=square(5,3)
print(obj.value())