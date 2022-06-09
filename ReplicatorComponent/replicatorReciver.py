import sys
sys.path.append('../')
import socket,pickle,time,random
from Model.DataModel import Data,CollectionDescription




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
readerSocket.connect((socket.gethostname(), 8000))



#Socket za primanje podataka od ReplicatorSender komponente
replicatorSocketReciever = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
replicatorSocketReciever.bind((socket.gethostname(), 10100))
replicatorSocketReciever.listen()

print("Waiting for data...")
conn, addr = replicatorSocketReciever.accept()
print('Connected by', addr)


historicalCollection = []
count = 0

while True:
    

    data = conn.recv(4096)
    data_variable = pickle.loads(data)  # ovde stize podatak tipa ("WriteRequest, data")

    if(data_variable.request == "WriteRequest"):

        print("Recieved from ReplicatorSender:")
        print(f"Code : {data_variable.data.code}   Value: {data_variable.data.value}")

        #pakovanje u cd klasu i slanje reader-u
        historicalCollection.append(Data(data_variable.data.value, data_variable.data.code))
        cd = CollectionDescription(historicalCollection,data_variable.data.code)
        print(F"Data Sent to Reader component...   CD DATASET = {cd.dataSet}")
        data_string = pickle.dumps(cd)
        readerSocket.send(data_string)
    
    elif data_variable.request == "ReadTable":
        data_string = pickle.dumps(data_variable.request)
        readerSocket.send(data_string)

    ''' 
    SLANJE LISTE PODATAKA

    historicalCollection.append(data_variable)

    count = count + 1

    if count == 10:
        print("Data Sent to Reader component...")
        print(historicalCollection)
        data_string = pickle.dumps(historicalCollection)
        readerSocket.send(data_string)
        historicalCollection.clear()
        count = 0
    
    '''
client.close()


     
