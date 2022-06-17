import sys
sys.path.append('../')
import socket,pickle,time
#from Database.CreateTables import CreateTables,CreateDatabase
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
        print(F"{dataRead1}\n{dataRead2}")

        result = [dataRead1,dataRead2]

        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((socket.gethostname(),1234))
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
        
