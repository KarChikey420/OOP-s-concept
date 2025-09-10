class Father:
    def __init__(self,name,properties):
        self.name=name
        self.properties=properties
        
    def information(self):
        return f"My name is {self.name} and my properties are {self.properties}"


class son(Father):
    def __init__(self,name,properties,extras):
        self.extras=extras
        super().__init__(name,properties)
        
    def information(self):
        parent_info=super().information()
        return f"{parent_info} and i have a {self.extras}"
        
obj=son("kartikey","cars","bicycle")
print(obj.information())