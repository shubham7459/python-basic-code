class shape:
    def Draw(self):
        print("Drawinf Shapre")
    
class circle(shape):
    def Draw(self):
        print("Drawing circle")
    
class square(shape):
    def Draw(self):
        print("Drawing Square")

c = circle()
s = square()

c.Draw()
s.Draw()