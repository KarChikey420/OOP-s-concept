class Animal:
    def __init__(self,name):
     self.name=name
    
    def sounds(self):
     return f"{self.name} sounds are:"
    
class Dog(Animal):
    def __init__(self,name):
        super().__init__(name)
        
    def sounds(self):
        return f"{self.name} is barking"
        
class Cat(Animal):
    def __init__(self,name):
      super().__init__(name)
    
    def sounds(self):  
      return f"{self.name} is meowing"


animal=Animal("Animal")
dog=Dog("Dog")
cat=Cat("cat")

print(animal.sounds())
print(dog.sounds())
print(cat.sounds())
