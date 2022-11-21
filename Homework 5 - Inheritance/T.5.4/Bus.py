from BusStation import BusStation

class Bus(BusStation): 
    __commuters = None
    __busstations = []
    def __init__(self, commuters, list_of_bussstations):
        super().__init__()
        self.__commuters = commuters
        self.__busstations = list_of_bussstations
    def startBusEngine(self):
        print("Engine started!")
    def getCommuters(self):
        return self.__commuters
    