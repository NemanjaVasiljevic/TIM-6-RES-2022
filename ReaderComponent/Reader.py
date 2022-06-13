import sys
sys.path.append('../')
<<<<<<< HEAD
from Database.DatabaseFunctions import (AddToTable)
import socket,pickle
from Model.DataModel import Data,Reader




r1 = Reader(8001,"dataset1")
clientSocket = r1.Connect()

    
while True:

    r1.WriteMessage(clientSocket,r1.database)
    
   
clientsocket.close()

''' Citanje iz baze poslednjih  vrednosti izabranih kodova

dataRead1, dataRead2 = r1.ReadData("CODE_DIGITAL", "CODE_ANALOG")
dataRead1 = Data(dataRead1[0],dataRead1[1])
dataRead2 = Data(dataRead2[0],dataRead2[1])
print(F"Value 1 : {dataRead1}\n Value 2: {dataRead2}")
 '''
=======
import socket,pickle,time
#from Database.CreateTables import CreateTables
from Model.DataModel import CollectionDescription, Data,Reader,Request,HistoricalValue


##### ovo se radi samo prvi put prilikom pokretanja posle samo zakomenterises
#CreateDatabase()
#CreateTables()
#############################################################################

'''
r1 = Reader("dataset1")
r2 = Reader("dataset2")
r3 = Reader("dataset3")
r4 = Reader("dataset4")

data = Data(369,"CODE_ANALOG")
if r1.CalculateDifference(data):
    r1.WriteData(data)
'''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(),8000))
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
                if r1.CalculateDifference(data):
                    print(f"Added to table {r1.database} => DATA : {data.code}   Value: {data.value}")
                    r1.WriteData(data)
                else:
                    print("Razlika je manja od 2% nece se upisati u bazu")


            elif dataSet == 2:               
                if r2.CalculateDifference(data):
                    print(f"Added to table {r2.database} => DATA : {data.code}   Value: {data.value}")
                    r2.WriteData(data)
                else:
                    print("Razlika je manja od 2% nece se upisati u bazu")
                

            elif dataSet == 3:             
                if r3.CalculateDifference(data):
                    print(f"Added to table {r3.database} => DATA : {data.code}   Value: {data.value}")
                    r3.WriteData(data)
                else:
                    print("Razlika je manja od 2% nece se upisati u bazu")


            elif dataSet == 4:               
                if r4.CalculateDifference(data):
                    print(f"Added to table {r4.database} => DATA : {data.code}   Value: {data.value}")
                    r4.WriteData(data)
                else:
                    print("Razlika je manja od 2% nece se upisati u bazu")


            counter = counter - 1 



    elif recived.request == "ReadTable":
        dataRead1, dataRead2 = r4.ReadData("CODE_CONSUMER", "CODE_SOURCE")
        dataRead1 = Data(dataRead1[0],dataRead1[1])
        dataRead2 = Data(dataRead2[0],dataRead2[1])
        print(F"{dataRead1}\n{dataRead2}")

        result = [dataRead1,dataRead2]

        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((socket.gethostname(),4321))
        result = pickle.dumps(result)
        s.send(result)
        s.close()


    elif recived.request == "ReadHistorical":

        print("Usao u ReadHistorical request")

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
        s.close()
        
>>>>>>> Branislav
