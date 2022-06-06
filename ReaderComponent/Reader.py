import sys
sys.path.append('../')
from Database.DatabaseFunctions import (AddToTable)
import socket,pickle
from Model.DataModel import Data,Reader




r1 = Reader(8001,"dataset1")
clientSocket = r1.Connect()

    
while True:

    r1.WriteMessage(clientSocket,r1.database)
    
   
clientsocket.close()

''' Citanje iz baze poslednjih  vrednosti izabranih kodova

dataRead1, dataRead2 = r1.ReadData("CODE_DIGITAL", "CODE_ANALOG")
dataRead1 = Data(dataRead1[0],dataRead1[1])
dataRead2 = Data(dataRead2[0],dataRead2[1])
print(F"Value 1 : {dataRead1.str()}\n Value 2: {dataRead2.str()}")
 '''