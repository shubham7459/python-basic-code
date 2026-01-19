class animal:
    def sound(self):
        print("Some generic sound")
class cat(animal):
    def sound(self):
        print("meoa!")


a = animal()
c = cat()
a.sound()
c.sound()