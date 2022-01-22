from abc import ABC, abstractmethod
class Bike(ABC):
    def Bill(self, amount):
        print("This month's payment is ",amount)

    def payment(self, amount):
        pass

class BikeMonthlyPayment(Bike):
    def monthlyPayment(self, amount):
        print('After this month\'s payment of {}, your total remaining due is $500 '.format(amount))

obj = BikeMonthlyPayment()
obj.Bill("$100")
obj.payment("$100")
        
        
    
