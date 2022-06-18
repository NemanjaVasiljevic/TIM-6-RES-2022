import sys
sys.path.append('../')
import socket,pickle,time,random
from Model.DataModel import Data,CollectionDescription, DeltaCD
from Logger.Logger import logWriter

#Socket sa prosledijivanje podataka Reader komponenti
readerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
readerSocket.connect((socket.gethostname(), 8000))



#Socket za primanje podataka od ReplicatorSender komponente
replicatorSocketReciever = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
replicatorSocketReciever.bind((socket.gethostname(), 10100))
replicatorSocketReciever.listen()

print("Waiting for data...")
conn, addr = replicatorSocketReciever.accept()
print('Connected by', addr)


historicalCollection = []
ADD=[]
UPDATE=[]
codes = []
countADD = 0
countUPDATE = 0

while True:
    

    data = conn.recv(4096)
    data_variable = pickle.loads(data)  # ovde stize podatak tipa ("WriteRequest, data")  data: value code

    if(data_variable.request == "WriteRequest"):

        print("Recieved from ReplicatorSender:")
        print(f"Code : {data_variable.data.code}   Value: {data_variable.data.value}")
        logWriter(f"Primio sadrzaj od REPLICATOR SENDER ({data_variable.data})","REPLICATOR RECIVER")

        #pakovanje u cd klasu i slanje reader-u
        historicalCollection.append(Data(data_variable.data.value, data_variable.data.code))
        cd = CollectionDescription(historicalCollection,data_variable.data.code)


        if data_variable.data.code in codes:
          UPDATE.append(cd)
        else:
            ADD.append(cd)     

        count = len(ADD) + len(UPDATE)

        if(count == 10):
            deltaCD = DeltaCD(ADD,UPDATE)

            data_variable.data = deltaCD.ADD + deltaCD.UPDATE
            data_string = pickle.dumps(data_variable)
            readerSocket.send(data_string)
            print("\nPOSLAO\n")
            ADD.clear()
            UPDATE.clear()
            count = 0

        codes = ADD + UPDATE

    
    elif data_variable.request == "ReadTable":
        data_string = pickle.dumps(data_variable)
        readerSocket.send(data_string)

    elif data_variable.request == "ReadHistorical":
        print("Dobio read request")
        data_string = pickle.dumps(data_variable)
        readerSocket.send(data_string)




     
