class Ractangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    
    def area(self):
        return f"Area Of Ractangle:{self.length*self.width}"
    
    def perimeter(self):
        return f"Perimeter Of Ractangle:{2*(self.length+self.width)}"
    
if __name__=="__main__":
    obj=Ractangle(20,30)
    print(obj.area())
    print(obj.perimeter())