class Student:
    def __init__(self,name,roll_number,marks):
        self.name=name
        self.roll_number=roll_number
        self.marks=marks
        
    def grade(self):
        if self.marks>90:
            return "Exellent"
        elif self.marks>70 and self.marks<90:
            return "Good"
        else:
            return "Need Improvement"
        
if __name__=="__main__":
    obj=Student("kartik",21,80)
    print(obj.grade())