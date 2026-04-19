class addition:
    def __init__(self, a, b):
        self.a=a
        self.b=b
        
    def add(self):
        return self.a + self.b

class submision(addition):
    def __init__(self,a,b,c):
        super().__init__(a,b)
        self.c=c
        
    def add(self):
        return self.a + self.b + self.c
    
if __name__ == "__main__":
    myobj=addition(1,2)
    print(myobj.add())
    
    myobj1=submision(1,2,3)
    print(myobj1.add())