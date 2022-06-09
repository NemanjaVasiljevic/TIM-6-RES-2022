import sys
sys.path.append('../')
import socket,pickle,time
#from Database.CreateTables import CreateTables
from Model.DataModel import CollectionDescription, Data,Reader,Request,HistoricalValue


##### ovo se radi samo prvi put prilikom pokretanja posle samo zakomenterises
#CreateDatabase()
#CreateTables()
#############################################################################

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
        #print("Usao u WriteRequest")
        CDArray = recived.data
        
        counter = 10

        for x in CDArray:

            dataSet = x.dataSet
            data = x.historicalCollection[-counter]
            if dataSet == 1:

                r1.WriteData(data)
                
            elif dataSet == 2:
                
                r2.WriteData(data)

            elif dataSet == 3:
                
                r3.WriteData(data)

            elif dataSet == 4:
                
                r4.WriteData(data)

            counter = counter - 1 

    elif recived.request == "ReadTable":
        dataRead1, dataRead2 = r4.ReadData("CODE_CONSUMER", "CODE_SOURCE")
        dataRead1 = Data(dataRead1[0],dataRead1[1])
        dataRead2 = Data(dataRead2[0],dataRead2[1])
        print(F"{dataRead1}\n{dataRead2}")












    '''
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(),8000))
    s.listen(1)
    print("Waiting for connection...")

    requestSocket, address = s.accept()
    print(f"Connection established from address {address}")

    data = requestSocket.recv(4098)
    #request = Request(pickle.loads(request)) #ovde je stigao samo request

    data = data.historicalCollection[-1]


    r1 = Reader(8001,"dataset1")
    #clientSocket1 = r1.Connect()
    r2 = Reader(8002,"dataset2")
    #clientSocket2 = r1.Connect()
    r3 = Reader(8003,"dataset3")
    #clientSocket3 = r1.Connect()
    r4 = Reader(8004,"dataset4")
    #clientSocket4 = r1.Connect()




    while True:


        
        if(request == "WriteRequest"):
            data = request.recv(4098)

            if(data.dataSet == 1):
                r1.ReciveData()
        
        else:
            dataRead1, dataRead2 = r1.ReadData("CODE_DIGITAL", "CODE_ANALOG")
            dataRead1 = Data(dataRead1[0],dataRead1[1])
            dataRead2 = Data(dataRead2[0],dataRead2[1])
            print(F"Value 1 : {dataRead1.str()}\n Value 2: {dataRead2.str()}")
            val = HistoricalValue("CODE_DIGITAL","2022-06-04 13:15:49", "2022-06-04 13:16:09")
            response = r1.ReadHistory(val)

            for x in response:
                print(F"Value: {x[0]} Code: {x[1]}")

        '''






