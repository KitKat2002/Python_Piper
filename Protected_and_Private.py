#Creates a class and a function with a protected number
class Number:
    def __init__(self):
        self._protectedNumber = 0
#Creates a function with a private number 
    def __init__(self):
        self.__privateNumber = 13
#Retrieves the private number "13"
    def getPrivateNumber(self):
        print(self.__privateNumber)

    def setPrivateNumber(self, private):
        self.__privateNumber = private
#Sets and retrieves the protected number to 7
obj = Number()
obj._protectedNumber = 7
print(obj._protectedNumber)
#Gets the private number and sets another private number to 24
obj = Number()
obj.getPrivateNumber()
obj.setPrivateNumber(24)
obj.getPrivateNumber()

