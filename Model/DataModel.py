from ast import Raise
import sys
sys.path.append('../')
import socket,pickle
from Database.DatabaseFunctions import (AddToTable)


class Data:
    def __init__(self, value, code):
        self.value = value
        self.code = code
    def __str__(self):
        return f"Code: {self.code} Value: {self.value}"    

class Reader:
    def __init__(self,port,database):
        self.port = port
        self.database = database

    def Connect(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((socket.gethostname(),self.port))
        s.listen(1)
        print("Waiting for connection...")

        clientsocket, address = s.accept()
        print(f"Connection established from address {address}")
        return clientsocket

    def WriteMessage(self,clientsocket,database):
        msg = clientsocket.recv(4098)
        data = pickle.loads(msg)
        try:
            print("Recieved from ReplicatorReciver:")
            print(f"Code : {data.historicalCollection[-1].code}   DataSet: {data.dataSet}")
            print("HistoricalCollection:")
            print(*data.historicalCollection, sep="\n")
            AddToTable(data.historicalCollection[-1].value, data.historicalCollection[-1].code, "dataset1")
            print("Succsessfully added object to the table")

        except:
            return F"Whoops. Something went wrong with writting in base!"
	
class CollectionDescription:
        def __init__(self,historicalCollection,code):
            if code == "CODE_ANALOG" or "CODE_DIGITAL":
                self.dataSet = 1
            elif code ==  "CODE_CUSTOM" or "CODE_LIMITSET":
                self.dataSet = 2
            elif code ==  "CODE_SINGLENOE" or "CODE_MULTIPLENODE":
                self.dataSet = 3
            elif code ==  "CODE_CONSUMER" or "CODE_SOURCE":
                self.dataSet = 4    

            self.historicalCollection = historicalCollection	
