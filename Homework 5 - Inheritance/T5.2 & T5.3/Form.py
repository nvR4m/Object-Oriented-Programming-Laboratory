class Form:
    __color = None 
    _name = None
    def _setColor(self, color):
        self.color = color
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name
    def setName(self):
        self.name = NameError
    def showMessage(self):
        print("messege from Form")
    def computeArea(self, width, length):
        return width * length
        
