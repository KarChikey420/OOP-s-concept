class Student:
    name="Anonymous" # Its a class variable because of priority is not that much 
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