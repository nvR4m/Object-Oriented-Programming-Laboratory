from Classes.Car import Car
class Driver:
    def __init__(self, name, age, hasDriverLicence, driverLicenceID, car):
        self.name = name
        self.age = age
        self.hasDriverLicence = hasDriverLicence
        self.driverLicenceID = driverLicenceID
        self.car = car
    
    def passDocuments(self):
        print("Name: " + self.name)
        if(self.hasDriverLicence):
            print("Driver Licence ID: " + self.driverLicenceID)
            if self.car.current_speed > 80:
                print("Ai fost prins cu o viteza de: " + str(self.car.current_speed))
                print("Ai ramas si fara permis!")
            else:
                print("Esti in limita legala! You can go!")
        else: 
            print("You don't have a driver licence!")
            print("Dosar penal, bafta!")
    
    def runFromPolice(self):
        if self.car.top_speed > 150:
            print("You run fast! You escaped the police!")
        else:
            print("You tried to run from the police. Unfortunatlly your car is slow! BUSTED!")