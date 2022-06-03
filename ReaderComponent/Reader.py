from gzip import READ
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
clientSocket = r1.Connect()

#dataRead = r1.ReadData("CODE_DIGITAL")

#for x in dataRead:
#    x = Data(x[0],x[1])
#    print(f"Podatak ")

while True:
   r1.WriteData(clientSocket,r1.database)
