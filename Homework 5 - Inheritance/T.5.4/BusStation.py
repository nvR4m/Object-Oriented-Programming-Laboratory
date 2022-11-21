class BusStation:
    __commuters = None 
    __name = None
    def __init__(self, commuters, name):
        self.__commuters = commuters
        self.__name = name
    def getCommuters(self):
        return self.__commuters