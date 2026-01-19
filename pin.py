class Mobile :
    def __init__ (self,name,pin):
        self.name = name
        self.__pin = pin
    def verify(self,veri):
        if(self.__pin == veri):
            return "verify"
        else :
            return "Incorrect"   

ak = Mobile("vivo",49)
print(ak.verify(49))
print(ak.verify(50))