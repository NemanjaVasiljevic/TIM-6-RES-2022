from CreateDatabase import CreateDatabase
from CreateTables import CreateTables
from DatabaseFunctions import (AddToTable)
import socket,pickle

HEADERSIZE = 10

##### ovo se radi samo prvi put prilikom pokretanja posle samo zakomenterises
#CreateDatabase()
#CreateTables()
#############################################################################

## problem kod importovanje Database foldera nece da ga vidi kao modul pa sam kopirao samo u ReaderComponent sve radi testiranja ispravnosti

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(),8080))

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")

    data = clientsocket.recv(16)