class Mobile :
    def __init__ (self,name,price):
        self.name = name
        self.__price = price
    def update(self,amount):
        self.__price = amount
    def display(self):
        return self.__price

ak = Mobile("vivo",1000000000)
ak.update(48)
print(ak.display())