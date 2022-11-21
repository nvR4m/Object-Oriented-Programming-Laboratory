from Form import Form
class Rectange(Form):
    _width = None
    _height = None
    def __init__(self, name, _width, _height):
        super().__init__(name)
        self._width = _width
        self._height = _height
    def setWidth(self, width):
        self._width = width
    def getWidth(self):
        return self._width
    def showMessage(self):
        print("messege from Rectange")
    def computeArea(self):
        return self._width * self._height

