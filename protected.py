# class Shape:
#     def __init__(self,num1,num2):
#         self._num1=num1
#         self._num2=num2
        
        
# class square(Shape):
#     # def __init__(self,num1,num2):
#     #     super().__init__(num1,num2)
    
#     def value(self):
#         return self._num1+self._num2


# obj=square(5,3)
# print(obj.value())

# class Father:
#     def __init__(self,name,work):
#         self._name=name
#         self._work=work
        
#     def _my_info(self):
#         return f"my name is {self._name} profession {self._work}"
    
#     def my_info(self):
#         return self._my_info()
    
# class son(Father):
#     def __init__(self, name, work):
#         super().__init__(name, work)
        
#     def my_info(self):
#         return super()._my_info()
    
# if __name__=="__main__":
    
#     obj=Father("deva","doctor")
#     print(obj.my_info())
#     obj1=son("deepu","dancer")
#     print(obj1.my_info())

class Parent:
    def __init__(self,name,age):
        self._name=name
        self._age=age
        
    def _detail(self):
        return f"my name {self._name} and age {self._age}"
    
    def detail(self):
        return self._detail()
    
class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name, age)
        
    def mydetail(self):
        return super()._detail() 
    
my_obj=Child('rooo','12')
print(my_obj.mydetail())