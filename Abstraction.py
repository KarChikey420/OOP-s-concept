class Car:
    def __init__(self):
        self.acc=False
        self.clutch=False
        self.brk=False
        
    def Start(self):
        self.clutch=True
        self.acc=True
        print("Car Start >>>>>>")
    
C1=Car()
C1.Start()