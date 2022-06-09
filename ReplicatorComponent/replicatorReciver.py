import sys
sys.path.append('../')
import socket,pickle,time,random
from Model.DataModel import Data
from Model.DataModel import CollectionDescription
from Model.DataModel import DeltaCD





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
readerSocket.connect((socket.gethostname(), 8001))



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


while True:

     data = conn.recv(4096)
     data_variable = pickle.loads(data)
     historicalCollection.append(data_variable)
    
     print("Recieved from ReplicatorSender:")
     print(data_variable)

     #pakovanje u cd klasu i slanje reader-u
     cd = CollectionDescription(historicalCollection,data_variable.code)
     if data_variable.code in codes:
          UPDATE.append(cd)
     else:
          ADD.append(cd)     

     if(ADD.count + UPDATE.count == 10):
          #print("Data Sent to Reader component...")
          #print(f"CODE : {data_variable.code}   DATASET : {cd.dataSet}")
          deltaCD = DeltaCD(ADD,UPDATE)
          addUpdate = deltaCD.ADD + deltaCD.UPDATE
          data_string = pickle.dumps(addUpdate)
          readerSocket.send(data_string)
     codes = ADD + UPDATE
     ADD.clear()
     UPDATE.clear()
client.close()