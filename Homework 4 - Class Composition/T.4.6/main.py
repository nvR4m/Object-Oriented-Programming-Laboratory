'''
HOMEWORK 4
IRIMIA ANDREI - CEN2.2A

6. A CAR IS STOPPED BY POLICE, SOME DOCUMENTS ARE NEEDED. BASED ON SOME ACTIONS ORGANIZE DATA.
'''
from Classes.Driver import Driver
from Classes.Car import Car

car1 = Car("Honda", "DJ11ABC", 70, 170, False)
drv1 = Driver("Gica", 20, True, "2312312312", car1)
car1.vizitaLaVericu()
drv1.runFromPolice()
