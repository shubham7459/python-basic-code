class student :
    def __init__ (self,name,salary):
        self.name = name
        self.__salary = salary
    def update(self,amount):
        self.__salary += amount
    def display(self):
        return self.__salary

ak = student("Tushar",1000000000)
ak.update(1)
print(ak.display())