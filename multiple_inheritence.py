class Fater:
    def __init__(self,name,properties):
        self.name=name
        self.properties=properties
        
    def Who(self):
        return f"i am {self.name} and my {self.properties}"
        

class Mother:
    def __init__(self,name,extras):
        self.name=name
        self.extras=extras
        
    def Who(self):
        return f"i am {self.name} and i have{self.extras}"
        
class Child(Fater,Mother):
    def __init__(self,name,properties,extras):
        Fater.__init__(self,name,properties)
        Mother.__init__(self,name,extras)
        
    def Who(self):
        return f"i am {self.name} and i have{self.properties} and {self.extras}"
        
child=Child("anna","cars","abroad land")
print(child.Who())