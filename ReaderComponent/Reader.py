import sys
sys.path.append('../')
import socket,pickle
#from Database.CreateTables import CreateTables
from Model.DataModel import Data,Reader


##### ovo se radi samo prvi put prilikom pokretanja posle samo zakomenterises
#CreateDatabase()
#CreateTables()
#############################################################################

r1 = Reader(8001,"dataset1")
#clientSocket1 = r1.Connect()
#r2 = Reader(8002,"dataset2")
#clientSocket2 = r1.Connect()
#r3 = Reader(8003,"dataset3")
#clientSocket3 = r1.Connect()
#r4 = Reader(8004,"dataset4")
#clientSocket4 = r1.Connect()




#while True:
#     r1.WriteData(clientSocket1,"dataset1")


dataRead1, dataRead2 = r1.ReadData("CODE_DIGITAL", "CODE_ANALOG")
dataRead1 = Data(dataRead1[0],dataRead1[1])
dataRead2 = Data(dataRead2[0],dataRead2[1])
print(F"Value 1 : {dataRead1.str()}\n Value 2: {dataRead2.str()}")


