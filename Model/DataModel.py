from ast import Raise
from asyncio.log import logger
import sys
sys.path.append('../')
import socket,pickle
from Database.DatabaseFunctions import (AddToTable)
from Database.DatabaseFunctions import (ReadFromTable)
from Logger import logger



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
        componentName = 'READER'
        logger.logWriter("Waiting for connection...", componentName)

        clientsocket, address = s.accept()
        logger.logWriter(f"Connection established from address {address}", componentName)
        return clientsocket

    def WriteMessage(self,clientsocket,database):
        msg = clientsocket.recv(4098)
        data = pickle.loads(msg)
        componentName = 'READER'
        try:
            logger.logWriter("Recieved from ReplicatorReciver:", componentName)
            logger.logWriter(f"Code : {data.historicalCollection[-1].code}   DataSet: {data.dataSet}", componentName)
            logger.logWriter("HistoricalCollection:", componentName)
            logger.logWriter(str(*data.historicalCollection, sep="\n"), componentName)
            AddToTable(data.historicalCollection[-1].value, data.historicalCollection[-1].code, "dataset1")
            logger.logWriter("Succsessfully added object to the table", componentName)

        except:
            logger.logWriter("Whoops. Something went wrong with writting in base!", componentName)
            return F"Whoops. Something went wrong with writting in base!"
	

    def ReadData(self,code1, code2):
        data1, data2 = ReadFromTable(code1,code2, self.database)
        return data1, data2


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

class HistoricalValue:
        def __init__(self, code, fromTime, toTime):
            self.code = code
            self.fromTime = fromTime
            self.toTime = toTime