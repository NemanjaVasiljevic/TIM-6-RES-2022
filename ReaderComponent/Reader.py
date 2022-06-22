import sys
from mysqlx import DatabaseError
sys.path.append('../')
import socket,pickle,time
#from Database.CreateTables import CreateTables,CreateDatabase
from Model.DataModel import CollectionDescription, Data,Request,HistoricalValue
from Logger.Logger import logWriter
from Database.DatabaseFunctions import *

##### ovo se radi samo prvi put prilikom pokretanja posle samo zakomenterises
#CreateDatabase()
#CreateTables()
#############################################################################

###########################################################
def WriteData(data,database,db):
        AddToTable(data.value, data.code, database,db)

def ReadData(code,database,db):
        try:
                data = ReadFromTable(code, database,db)
                return data
        except DatabaseError:
                return DatabaseError


def ReadHistory(historicalValue,database,db):
        try:
                retVal = ReadHistorical(historicalValue,database,db)
                return retVal

        except DatabaseError:
                return DatabaseError


def CalculateDifference(new,database,db):

        try:
                if new.code == "CODE_DIGITAL":
                        return True
        except AttributeError:
                return -1

        old = ReadFromTable(new.code, database,db)
        
        if old is None:
                print("Prvi prolaz jos nista nema u bazi")
                return True

        oldData = Data(old[0],old[1])
        difference = float(oldData.value) * 0.02

        print(F"\nGornja granica: {float(oldData.value) + difference} Donja granica: {float(oldData.value) - difference} Nova vrednost: {new} Stara vrednost: {oldData}\n")

        if(new.value > float(oldData.value) + difference or new.value < float(oldData.value) - difference):
                return True
        else:
                return False
        
def SocketConnect():
        try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.bind((socket.gethostname(),9999))
                s.listen(1)
                print("Waiting for connection...")

                replicatorSocket, address = s.accept()
                print(f"Connection established from address {address}")
                
                return replicatorSocket
        except socket.error:
                exit()
                
def ReciveData(socket):
        try:
                msg = socket.recv(4098)
                recived = pickle.loads(msg)
                return recived
        except EOFError:
                return None
        except ConnectionAbortedError:
                return None

def WriteInDatabase(CDArray,db):
        counter = 10

        for x in CDArray:

                dataSet = x.dataSet
                data = x.historicalCollection[-counter]

                if dataSet == 1:
                        if CalculateDifference(data,"dataset1",db):
                                logWriter(f"Added to table dataset1 => DATA : {data.code}   Value: {data.value}","READER")
                                WriteData(data,"dataset1",db)
                        else:
                                logWriter("Razlika je manja od 2% nece se upisati u bazu","READER")


                elif dataSet == 2:               
                        if CalculateDifference(data,"dataset2",db):
                                logWriter(f"Added to table dataset2 => DATA : {data.code}   Value: {data.value}","READER")
                                WriteData(data,"dataset2",db)
                        else:
                                logWriter("Razlika je manja od 2% nece se upisati u bazu","READER")
                        

                elif dataSet == 3:             
                        if CalculateDifference(data,"dataset3",db):
                                logWriter(f"Added to table dataset3 => DATA : {data.code}   Value: {data.value}","READER")
                                WriteData(data,"dataset3",db)
                        else:
                                logWriter("Razlika je manja od 2% nece se upisati u bazu","READER")


                elif dataSet == 4:               
                        if CalculateDifference(data,"dataset4",db):
                                logWriter(f"Added to table dataset4 => DATA : {data.code}   Value: {data.value}","READER")
                                WriteData(data,"dataset4",db)
                        else:
                                logWriter("Razlika je manja od 2% nece se upisati u bazu","READER")


                counter = counter - 1 

def ReadLastValues(recived,db):
        
        dataRead2=recived.data.code
        dataRead1=recived.data.value

        if dataRead1 == "CODE_ANALOG" or dataRead1 == "CODE_DIGITAL" :
                result1 = ReadData(dataRead1,"dataset1",db)
        
        elif dataRead1 ==  "CODE_CUSTOM" or dataRead1 == "CODE_LIMITSET":
                result1 = ReadData(dataRead1,"dataset2",db)

        elif dataRead1 == "CODE_SINGLENOE" or dataRead1 == "CODE_MULTIPLENODE":
                result1 = ReadData(dataRead1,"dataset3",db)

        elif dataRead1 == "CODE_CUSTOMER" or dataRead1 == "CODE_CONSUMER":
                result1 = ReadData(dataRead1,"dataset4",db)

        if dataRead2 == "CODE_ANALOG" or dataRead2 == "CODE_DIGITAL" :
                result2 = ReadData(dataRead2,"dataset1",db)
        
        elif dataRead2 ==  "CODE_CUSTOM" or dataRead2 == "CODE_LIMITSET":
                result2 = ReadData(dataRead2,"dataset2",db)

        elif dataRead2 == "CODE_SINGLENOE" or dataRead2 == "CODE_MULTIPLENODE":
                result2 = ReadData(dataRead2,"dataset3",db)

        elif dataRead2 == "CODE_CUSTOMER" or dataRead2 == "CODE_CONSUMER":
                result2 = ReadData(dataRead2,"dataset4",db)

        dataRead1 = Data(result1[0],result1[1])
        dataRead2 = Data(result2[0],result2[1])
        logWriter(f"Read from database => DATA : {dataRead1.code}   Value: {dataRead1.value}","READER")
        logWriter(f"Read from database => DATA : {dataRead2.code}   Value: {dataRead2.value}","READER")

        result = [dataRead1,dataRead2]
        
        # vracanje rezultata klijentu
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((socket.gethostname(),1234))
        result = pickle.dumps(result)
        s.send(result)
        
def ReadFromTableUsingTimeStamp(recived,db):
        if recived.data.code == "CODE_ANALOG" or recived.data.code == "CODE_DIGITAL" :
                result = ReadHistory(recived.data,"dataset1",db)
        
        elif recived.data.code ==  "CODE_CUSTOM" or recived.data.code == "CODE_LIMITSET":
                result = ReadHistory(recived.data,"dataset2",db)

        elif recived.data.code == "CODE_SINGLENOE" or recived.data.code == "CODE_MULTIPLENODE":
                result = ReadHistory(recived.data,"dataset3",db)

        elif recived.data.code == "CODE_CUSTOMER" or recived.data.code == "CODE_CONSUMER":
                result = ReadHistory(recived.data,"dataset4",db)

        #Slanje konzoli
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((socket.gethostname(),1234))
        result = pickle.dumps(result)
        s.send(result)
##################################################

def main():

        soket = SocketConnect()
        db = ConnectDatabase()
        while True:
                recived = ReciveData(soket)
                if recived.request == "WriteRequest":
                        WriteInDatabase(recived.data,db)
                        
                elif recived.request == "ReadTable":
                        ReadLastValues(recived,db)


                elif recived.request == "ReadHistorical":
                        ReadFromTableUsingTimeStamp(recived,db)
                        
        
if __name__ == '__main__':
        main()