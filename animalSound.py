class animal:
    def Draw(self):
        print("Drawinf Shapre")
    
class cow(animal):
    def Draw(self):
        print("mOOOOOOOOO!")
    
class lion(animal):
    def Draw(self):
        print("raayaraaaa!")

c = cow()
s = lion()

c.Draw()
s.Draw()