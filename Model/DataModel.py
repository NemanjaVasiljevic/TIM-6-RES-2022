from ast import Raise
import sys
sys.path.append('../')
import socket,pickle
from Database.DatabaseFunctions import (AddToTable)
from Database.DatabaseFunctions import (ReadFromTable)

listCodes = ["CODE_ANALOG","CODE_DIGITAL","CODE_CUSTOM","CODE_LIMITSET","CODE_SINGLENOE","CODE_MULTIPLENODE","CODE_CONSUMER","CODE_SOURCE"]


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
        s.listen()
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
            AddToTable(data.historicalCollection[-1].value, data.historicalCollection[-1].code,database)
            print("Succsessfully added object to the table")
        except:
            return F"Whoops. Something went wrong with writting in base!"
        

    def ReadData(self,code1, code2):
        data1, data2 = ReadFromTable(code1,code2, self.database)
        return data1, data2


class CollectionDescription:
        def __init__(self,historicalCollection,code):
            if code ==listCodes[0] or code == listCodes[1] :
                self.dataSet = 1
                #print("Usao u dataset1")
            elif code ==  listCodes[2] or code == listCodes[3]:
                self.dataSet = 2
                #print("Usao u dataset2")

            elif code == listCodes[4] or code == listCodes[5]:
                self.dataSet = 3
                #print("Usao u dataset3")

            elif code ==listCodes[6] or code == listCodes[7]:
                self.dataSet = 4
                #print("Usao u dataset4")
            else:
                self.dataSet = 0

            self.historicalCollection = historicalCollection

class HistoricalValue:
        def __init__(self, code, fromTime, toTime):
            self.code = code
            self.fromTime = fromTime
            self.toTime = toTime