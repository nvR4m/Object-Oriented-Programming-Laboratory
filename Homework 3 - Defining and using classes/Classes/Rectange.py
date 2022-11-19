class Rectangle: 
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def computePerimeter(self):
        self.perimeter = 2*(self.length + self.width)
        return self.perimeter
    def computeArea(self):
        self.area = self.length * self.width
        return self.area