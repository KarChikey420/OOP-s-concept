class Account:
    def __init__(self,balance,a_number):
        self.balance=balance
        self.a_number=str(a_number)
        
    def debit(self,amount):
        self.balance-=amount
        print(f"Rs. {amount} was debited")
        
    def Credit(self,amount):
        self.balance+=amount
        print(f"Rs. {amount} was credited")
    
    def get_balance(self):
        print(f"your current balance is {self.balance}")
        
A1=Account(5000,"007574")
A1.debit(1000)
A1.Credit(5000)
A1.get_balance()