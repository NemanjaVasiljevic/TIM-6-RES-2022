import sys
sys.path.append('../')
import socket,pickle,time,random
<<<<<<< HEAD
from Model.DataModel import Data
from Model.DataModel import CollectionDescription
=======
from Model.DataModel import Data,CollectionDescription, DeltaCD
>>>>>>> Branislav




#1.	CODE_ANALOG
#2.	CODE_DIGITAL
#3.	CODE_CUSTOM
#4.	CODE_LIMITSET
#5.	CODE_SINGLENOE
#6.	CODE_MULTIPLENODE
#7.	CODE_CONSUMER
#8.	CODE_SOURCE


#listNames = ["CODE_ANALOG","CODE_DIGITAL","CODE_CUSTOM","CODE_LIMITSET","CODE_SINGLENOE","CODE_MULTIPLENODE","CODE_CONSUMER","CODE_SOURCE"]

# Create a socket connection.
#Socket sa prosledijivanje podataka Reader komponenti
readerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
<<<<<<< HEAD
readerSocket.connect((socket.gethostname(), 8001))
=======
readerSocket.connect((socket.gethostname(), 8000))
>>>>>>> Branislav



#Socket za primanje podataka od ReplicatorSender komponente
replicatorSocketReciever = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
replicatorSocketReciever.bind((socket.gethostname(), 10100))
replicatorSocketReciever.listen()

print("Waiting for data...")
conn, addr = replicatorSocketReciever.accept()
print('Connected by', addr)

<<<<<<< HEAD
historicalCollection = []



while True:

     data = conn.recv(4096)
     data_variable = pickle.loads(data)
     historicalCollection.append(data_variable)
    
     print("Recieved from ReplicatorSender:")
     print(data_variable)

     #pakovanje u cd klasu i slanje reader-u
     cd = CollectionDescription(historicalCollection,data_variable.code)
     print("Data Sent to Reader component...")
     data_string = pickle.dumps(cd)
     readerSocket.send(data_string)
    
    

client.close()
=======

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

        #pakovanje u cd klasu i slanje reader-u
        historicalCollection.append(Data(data_variable.data.value, data_variable.data.code))
        cd = CollectionDescription(historicalCollection,data_variable.data.code)

        print(F"CD izgleda ovako: {cd.dataSet} {cd.historicalCollection[-1]}")

        if data_variable.data.code in codes:
          UPDATE.append(cd)
        else:
            ADD.append(cd)     

        count = len(ADD) + len(UPDATE)

        if(count == 10):
            #print("Data Sent to Reader component...")
            #print(f"CODE : {data_variable.code}   DATASET : {cd.dataSet}")
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


client.close()


     
>>>>>>> Branislav
