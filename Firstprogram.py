class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        
    def display(self):
        print("store data in database........")
        print(f"name is {self.name} || marks is {self.marks}")

S1=Student()
S1.display("Ram",400)
S1.display("Shyam",4000)