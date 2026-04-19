class Salary:
    def __init__(self,payout):
        self.payout=payout
    
    def Month1(self):
        print("Amount:",self.payout)
        
class Salary2(Salary):
    def __init__(self,payout,health_allounce):
        super().__init__(payout)
        self.health_allounce=health_allounce
        
    def Month2(self):
        print("amount:",self.health_allounce+self.payout)
        
class Salary3(Salary2):
    def __init__(self,intrest,payout,health_allounce):
        super().__init__(payout,health_allounce)
        self.intrest=intrest
        
    def overall(self):
        print("Total amount of money:",self.health_allounce+self.payout+self.intrest)
        
if __name__=="__main__":
    Obj=Salary3(1000,50000,5000)
    Obj.overall()