class RectangularPrism:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
        
    def volume(self):
        volume = self.length * self.width * self.height 
        return volume

print("Pick A Number")
height = int(input())
print("Pick Another")
width = int(input())
print("Pick One More")
length = int(input())


answer = RectangularPrism(height, width, length)

print("your answer is... %s!" %answer.volume())
    




