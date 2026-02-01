class Info:
    myname="Kartikey"
    
    @classmethod
    def name(cls):
        print(f"my name is {cls.myname}")
    
I=Info()
I.name()