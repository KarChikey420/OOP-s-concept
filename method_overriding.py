class addition:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
        
    def operation(self):
        return self.num1+self.num2
        
class subtraction(addition):
    def __init__(self,num1,num2):
        super().__init__(num1,num2)
        
    def operation(self):
        return self.num1-self.num2
        
add=addition(2,4)
sub=subtraction(4,2)

print(sub.operation())