from Classes.BusStation import BusStation

class Bus:
    def __init__(self, licence_place, passangers):
        self.licence_place = licence_place
        self.passangers = passangers
    def pickUpPassangers(self, station):
        old_pass = self.passangers
        self.passangers += station.passangers_in_station
        if self.passangers >= 25:
            station.passangers_in_station -= 25 - old_pass
            print("Number of passangers excedeed the limit!")
            self.passangers = 25
        else: 
            print("New passangers in bus!")
            station.passangers_in_station = 0
    def removePassangers(self, station, nr_passangers_removed):
        self.passangers -= nr_passangers_removed
        station.passangers_in_station = nr_passangers_removed
        if self.passangers < 0:
            print("All passangers left the bus!")
            self.passangers = 0
        else: 
            print(str(nr_passangers_removed) + " left the bus!")
    def showPassangers(self):
        print("There are currentlly " + str(self.passangers) + " in the bus!")


        