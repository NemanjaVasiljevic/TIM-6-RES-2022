import sys
sys.path.append('../')
import socket,pickle,time,random
from Model.DataModel import Data
from Model.DataModel import CollectionDescription
from Logger import logger



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
componentName = 'REPLICATOR RECEIVER'

logger.logWriter("Waiting for data...", componentName)
conn, addr = replicatorSocketReciever.accept()
logger.logWriter('Connected by' + str(addr), componentName)

historicalCollection = []




while True:

     data = conn.recv(4096)
     data_variable = pickle.loads(data)
     historicalCollection.append(data_variable)
     log = "Recieved from ReplicatorSender:"
     log += str(data_variable)

     logger.logWriter(log, componentName)

     #pakovanje u cd klasu i slanje reader-u
     cd = CollectionDescription(historicalCollection,data_variable.code)
     #print("Data Sent to Reader component...")
     data_string = pickle.dumps(cd)
     readerSocket.send(data_string)
     logger.logWriter("Data Sent to Reader component", componentName)
    

client.close()