class student :
    def __init__ (self,name,marks):
        self.name = name
        self.__marks = marks
    def display(self):
        return self.__marks

ak = student("Tushar",39)
print(ak.display())