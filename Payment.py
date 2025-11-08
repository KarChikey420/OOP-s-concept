from abc import ABC,abstractmethod

class Payment:
    def __init__(self,method_name):
        self.method_name=method_name
    
    @abstractmethod
    def pay(self,amount):
        pass
    
class CreditCardPayment(Payment):
    def __init__(self,card_number):
        super().__init__("crdit_card")
        self.card_number=card_number
    
    def pay(self,amount):
        print(f"Using {self.method_name} ({self.card_number} to pay amount {amount})")
        
class UPIPayment(Payment):
    def __init__(self, upi_id): 
        super().__init__("UPI") 
        self.upi_id = upi_id
         
    def pay(self, amount): 
        print(f"Using {self.method_name} ({self.upi_id}) to pay ₹{amount}") 
        print("UPI payment successful!") 

cc = CreditCardPayment("1234-5678-9999")
cc.pay(1000)
upi = UPIPayment("karan@upi") 
upi.pay(500) 