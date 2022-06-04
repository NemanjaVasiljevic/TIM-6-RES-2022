from ast import Raise
import sys
sys.path.append('../')
import socket,pickle
from Database.DatabaseFunctions import (AddToTable, ReadFromTable)


class Data:
    def __init__(self, value, code):
        self.value = value
        self.code = code

#########################################################################################################
class Reader:
    def __init__(self,port,database):
        self.port = port
        self.database = database


    def Connect(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind((socket.gethostname(),self.port))
            s.listen(1)
            print("Waiting for connection...")

            clientsocket, address = s.accept()
            print(f"Connection established from address {address}")
            return clientsocket
        except:
            return F"Connection failed."


    def WriteData(self,clientsocket,database):

        msg = clientsocket.recv(4098)
        data = pickle.loads(msg)

        for x in data:
            try:
                AddToTable(x.value, x.code, database)
                print("Recieved from ReplicatorReciver:")
                print(f"Code : {x.code}   Value: {x.value}")

            except:
                return F"Whoops. Something went wrong with writting in base!"


    def ReadData(self,code):
        data = []
        data = ReadFromTable(code, self.database)
        return data
#########################################################################################################