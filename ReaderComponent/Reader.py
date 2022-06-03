import sys
sys.path.append('../')
from Database.DatabaseFunctions import (AddToTable)
from Database.CreateDatabase import CreateDatabase
from Database.CreateTables import CreateTables
import socket,pickle
from Model.DataModel import Data,Reader


##### ovo se radi samo prvi put prilikom pokretanja posle samo zakomenterises
#CreateDatabase()
#CreateTables()
#############################################################################

r1 = Reader(8001,"dataset1")
clientSocket = r1.Connect()

while True:
    r1.WriteData(clientSocket,r1.database)
