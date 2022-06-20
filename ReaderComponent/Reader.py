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
class Reader:
    def __init__(self,database):
        self.database = database

def WriteData(data,database):
        try:
                AddToTable(data.value, data.code, database)
                return 1
        except:
                return -1


def ReadData(code,database):
        try:
                data = ReadFromTable(code,"", database)
                return data
        except:
                return -1


def ReadHistory(historicalValue,database):
        try:
                retVal = ReadHistorical(historicalValue,database)
                return retVal

        except:
                return -1


def CalculateDifference(new,database):

        if new.code == "CODE_DIGITAL":
                return True


        try:
                old = ReadFromTable(new.code,"", database)

        except:
                return -1

                
        if type(old) is None:
                print("Prvi prolaz jos nista nema u bazi")
                return True

        oldData = Data(old[0],old[1])
        difference = float(oldData.value) * 0.02

        print(F"\nGornja granica: {float(oldData.value) + difference} Donja granica: {float(oldData.value) - difference} Nova vrednost: {new} Stara vrednost: {oldData}\n")

        if(new.value > float(oldData.value) + difference or new.value < float(oldData.value) - difference):
                return True
        else:
                return False
##################################################


def main():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((socket.gethostname(),8001))
        s.listen(1)
        print("Waiting for connection...")

        replicatorSocket, address = s.accept()
        print(f"Connection established from address {address}")

        r1 = Reader("dataset1")
        r2 = Reader("dataset2")
        r3 = Reader("dataset3")
        r4 = Reader("dataset4")

        while True:
                msg = replicatorSocket.recv(4098)
                recived = pickle.loads(msg)

                if recived.request == "WriteRequest":
                        CDArray = recived.data
                        
                        counter = 10

                        for x in CDArray:

                                dataSet = x.dataSet
                                data = x.historicalCollection[-counter]

                                if dataSet == 1:
                                        if CalculateDifference(data,r1.database):
                                                logWriter(f"Added to table {r1.database} => DATA : {data.code}   Value: {data.value}","READER")
                                                WriteData(data,r1.database)
                                        else:
                                                logWriter("Razlika je manja od 2% nece se upisati u bazu","READER")


                                elif dataSet == 2:               
                                        if r2.CalculateDifference(data,r2.database):
                                                logWriter(f"Added to table {r2.database} => DATA : {data.code}   Value: {data.value}","READER")
                                                r2.WriteData(data,r2.database)
                                        else:
                                                logWriter("Razlika je manja od 2% nece se upisati u bazu","READER")
                                        

                                elif dataSet == 3:             
                                        if r3.CalculateDifference(data,r3.database):
                                                logWriter(f"Added to table {r3.database} => DATA : {data.code}   Value: {data.value}","READER")
                                                r3.WriteData(data,r3.database)
                                        else:
                                                logWriter("Razlika je manja od 2% nece se upisati u bazu","READER")


                                elif dataSet == 4:               
                                        if r4.CalculateDifference(data,r4.database):
                                                logWriter(f"Added to table {r4.database} => DATA : {data.code}   Value: {data.value}","READER")
                                                r4.WriteData(data,r4.database)
                                        else:
                                                logWriter("Razlika je manja od 2% nece se upisati u bazu","READER")


                                counter = counter - 1 



                elif recived.request == "ReadTable":
                        dataRead2=recived.data.code
                        dataRead1=recived.data.value

                        if dataRead1 == "CODE_ANALOG" or dataRead1 == "CODE_DIGITAL" :
                                result1 = r1.ReadData(dataRead1)
                        
                        elif dataRead1 ==  "CODE_CUSTOM" or dataRead1 == "CODE_LIMITSET":
                                result1 = r2.ReadData(dataRead1)

                        elif dataRead1 == "CODE_SINGLENOE" or dataRead1 == "CODE_MULTIPLENODE":
                                result1 = r3.ReadData(dataRead1)

                        elif dataRead1 == "CODE_CUSTOMER" or dataRead1 == "CODE_CONSUMER":
                                result1 = r4.ReadData(dataRead1)

                        if dataRead2 == "CODE_ANALOG" or dataRead2 == "CODE_DIGITAL" :
                                result2 = r1.ReadData(dataRead2)
                        
                        elif dataRead2 ==  "CODE_CUSTOM" or dataRead2 == "CODE_LIMITSET":
                                result2 = r2.ReadData(dataRead2)

                        elif dataRead2 == "CODE_SINGLENOE" or dataRead2 == "CODE_MULTIPLENODE":
                                result2 = r3.ReadData(dataRead2)

                        elif dataRead2 == "CODE_CUSTOMER" or dataRead2 == "CODE_CONSUMER":
                                result2 = r4.ReadData(dataRead2)

                        dataRead1 = Data(result1[0],result1[1])
                        dataRead2 = Data(result2[0],result2[1])
                        logWriter(f"Read from database => DATA : {dataRead1.code}   Value: {dataRead1.value}","READER")
                        logWriter(f"Read from database => DATA : {dataRead2.code}   Value: {dataRead2.value}","READER")

                        result = [dataRead1,dataRead2]

                        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                        s.connect((socket.gethostname(),1234))
                        result = pickle.dumps(result)
                        s.send(result)


                elif recived.request == "ReadHistorical":

                        if recived.data.code == "CODE_ANALOG" or recived.data.code == "CODE_DIGITAL" :
                                result = r1.ReadHistory(recived.data)
                        
                        elif recived.data.code ==  "CODE_CUSTOM" or recived.data.code == "CODE_LIMITSET":
                                result = r2.ReadHistory(recived.data)

                        elif recived.data.code == "CODE_SINGLENOE" or recived.data.code == "CODE_MULTIPLENODE":
                                result = r3.ReadHistory(recived.data)

                        elif recived.data.code == "CODE_CUSTOMER" or recived.data.code == "CODE_CONSUMER":
                                result = r4.ReadHistory(recived.data)

                        #Slanje konzoli
                        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                        s.connect((socket.gethostname(),1234))
                        result = pickle.dumps(result)
                        s.send(result)
        
if __name__ == '__main__':
        main()