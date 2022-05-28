import sys
sys.path.append('../')
from Database.DatabaseFunctions import (AddToTable)
from Database.CreateDatabase import CreateDatabase
from Database.CreateTables import CreateTables
import socket,pickle
from DataModel import Data


##### ovo se radi samo prvi put prilikom pokretanja posle samo zakomenterises
#CreateDatabase()
#CreateTables()
#############################################################################

## problem kod importovanje Database foldera nece da ga vidi kao modul pa sam kopirao samo u ReaderComponent sve radi testiranja ispravnosti

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(),8081))
s.listen(1)
print("Waiting for connection...")

clientsocket, address = s.accept()
print(f"Connection established from address {address}")

while True:

    msg = clientsocket.recv(4098)
    data = pickle.loads(msg)
    AddToTable(data.value, data.code)
   
clientsocket.close();