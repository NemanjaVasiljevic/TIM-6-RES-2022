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

r1 = Reader(8001, "dataset1")
r2 = Reader(8002, "dataset2")
r3 = Reader(8003, "dataset3")
r4 = Reader(8004, "dataset4")

while True:
    data = replicatorSocket.recv(4098)
    data = pickle.loads(data)

    if(type(data) is CollectionDescription):
        value = data.historicalCollection[-1]
        dataSet = data.dataSet
        print("Recieved from ReplicatorReciver:")
        print(f"Code : {value.code}   Value: {value.value} writing into dataset{dataSet}")

        if dataSet == 1:

            r1.WriteData(value)
            
        elif dataSet == 2:
            
            r2.WriteData(value)

        elif dataSet == 3:
            
            r3.WriteData(value)

        elif dataSet == 4:
            
            r4.WriteData(value)

    elif data == "ReadTable":
        dataRead1, dataRead2 = r1.ReadData("CODE_DIGITAL", "CODE_ANALOG")
        dataRead1 = Data(dataRead1[0],dataRead1[1])
        dataRead2 = Data(dataRead2[0],dataRead2[1])
        print(F"Value 1 : {dataRead1.str()}\n Value 2: {dataRead2.str()}")
        time.sleep(3)












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






