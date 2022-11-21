'''
HOMEWORK 4
IRIMIA ANDREI - CEN2.2A

7. DEFINE CLASS BUS, BUSSTATION
'''
from Classes.Bus import Bus
from Classes.BusStation import BusStation

st1 = BusStation("Orizont", 3)
st2 = BusStation("Calu' Mort", 6)

bus1 = Bus("OT11ABF", st1)
bus1.showPassangers()