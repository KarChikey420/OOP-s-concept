from abc import ABC,abstractmethod

class Payment:
    def __init__(self,method_name):
        self.method_name=method_name
        
    @abstractmethod
    def pay(self,amount):
        pass

class CreditCardPayment(Payment):
    def __init__(self, method_name):
        super().__init__(method_name)
    
    def pay(self,amount):
        print(f"Using {self.method_name} to pay amount {amount}")
    
if __name__ == "__main__":
    cc=CreditCardPayment("credit_card")
    cc.pay(1000)