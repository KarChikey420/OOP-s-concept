class grandparent:
    def __init__(self,name,properties):
        self.name=name
        self.properties=properties
        
    def Who(self):
        return f"i am {self.name} and my {self.properties}"
        

class Father(grandparent):
    def __init__(self,name,properties,extras):
        super().__init__(name,properties)
        self.extras=extras
        
    def Who(self):
        return f"i am {self.name} and i have {self.properties} and {self.extras}"
        
class Child(Father):
    def __init__(self,name,properties,extras):
        super().__init__(name,properties,extras)
        
    def Who(self):
        return f"i am {self.name} and i have{self.properties} and {self.extras}"
        
child=Child("anna","cars","abroad land")
print(child.Who())