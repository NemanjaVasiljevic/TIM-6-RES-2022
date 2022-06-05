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
