#Makes use of the protected attribute
class Protected:
    def __init__(self):
        self._protectedVar = 0

obj = Protected()
obj.protectedVar = 4
print(obj.protectedVar)


#Makes use of the private attribute
class Private:
    def __init__(self):
        self.__privateVar = 41

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar = private

obj = Private()
obj.getPrivate()
obj.setPrivate(37)
obj.getPrivate()
