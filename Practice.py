from abc import ABC, abstractmethod

class Payment(ABC):
    def __init__(self, method_name):
        self.method_name = method_name
    
    @abstractmethod
    def process_payment(slef, amount):
        pass
    
class CreditCardPayment(Payment):
    def __init__(self, method_name):
        super().__init__(method_name)
    
    def process_payment(self, amount):
        print(f"Using {self.method_name} to process payment of amount {amount}")

if __name__ =="__main__":
    cc = CreditCardPayment("Credit Card")
    cc.process_payment(1000)