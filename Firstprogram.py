class Student:
    name="Anonymous" # Its a class variable its priority is less than instance variable
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        
    def display(self):
        print("store data in database........")
        print(f"name is {self.name} || marks is {self.marks}")

S1=Student("Ram",300)
S1.display()

S2=Student("Shyam",400)
S2.display()