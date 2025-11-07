class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
class Employee(Person):
    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.salary=salary
    
    def Details(self):
        return f"My Name Is {self.name} And Age {self.age} And Salary {self.salary}"
    
if __name__=="__main__":
    obj=Employee("Kartik",12,2000000)
    print(obj.Details())