class Avarage:
    def __init__(self,name,marks,Avg):
        self.name=name
        self.marks=marks
        self.Avg=Avg
        
    def Student(self):
        sum=0
        for i in self.marks:
            sum+=i
        self.Avg=sum/len(self.marks)
        print(f"Hello ! {self.name} your AVG of Marks is {self.Avg}")
        
A1=Avarage("ghanshyam",[90,80,70,60],0)
A1.Student()