from ast import Raise
from msilib.schema import Error
import sys
sys.path.append('../')
import socket,pickle
from Database.DatabaseFunctions import (AddToTable, ReadFromTable, ReadHistorical)


class Request:
    def __init__(self,request,data):
        self.request = request
        self.data = data


#########################################################################################################

class Data:
    def __init__(self, value, code):
        self.value = value
        self.code = code
    def str(self):
        return f"Code: {self.code} Value: {self.value}"


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


    def ReadData(self,code1, code2):
        try:
            data1, data2 = ReadFromTable(code1,code2, self.database)
            return data1, data2
        except:
            return Error

    def ReadHistory(self,historicalValue):
        try:
            retVal = ReadHistorical(historicalValue,self.database)
            return retVal

        except:
            return print(F"Greska u ReadHistory")


#########################################################################################################


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



#########################################################################################################
class HistoricalValue:
        def __init__(self, code, fromTime, toTime):
            self.code = code
            self.fromTime = fromTime
            self.toTime = toTime

