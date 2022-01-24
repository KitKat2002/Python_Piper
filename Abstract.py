#Imports abstract method
from abc import ABC, abstractmethod
class Bike(ABC):
    def Bill(self, amount):
        print("This month's payment is ",amount)
#Utilizes abstract method
    @abstractmethod    
    def payment(self, amount):
        pass
#utilizes information from parent class
class BikeMonthlyPayment(Bike):
    def payment(self, amount):
        print('After this month\'s payment of {}, your total remaining due is $500 '.format(amount))

obj = BikeMonthlyPayment()
obj.Bill("$100")
obj.payment("$100")
        
        
    
