class Bird:
    def __init__(self):
        pass
    
    def fly(self):
        return "Bird flies in the sky"

class Airplane(Bird):
    def __init__(self):
        pass
    
    def fly(self):
        return "Airplane flies using engines"
    
if __name__=="__main__":
    obj=Airplane()
    print(obj.fly())