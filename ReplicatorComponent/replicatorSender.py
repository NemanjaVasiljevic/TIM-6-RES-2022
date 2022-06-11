import sys
sys.path.append('../')
import socket,pickle,time,random
from Model.DataModel import Data
from Logger import logger




#Socket za primanje podataka od Writer komponente
writerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
writerSocket.bind((socket.gethostname(), 8000))
writerSocket.listen()

#Socket za komunikaciju sa ReplicatorReciever komponentom
replicatorSocketSender= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
replicatorSocketSender.connect((socket.gethostname(),10100))

componentName = 'REPLICATOR SENDER'

logger.logWriter("Waiting for the Writer to send data...", componentName)
conn, addr = writerSocket.accept()
logger.logWriter('Connected by' + str(addr), componentName)

while True:
    
    data = conn.recv(4096)
    data_variable = pickle.loads(data)
    log = "Recieved from Writer:"
    if(type(data_variable) is Data): 
        log += str(data_variable)
        logger.logWriter(log, componentName)
        # Pickle the object and send it to ReplicatorReciever
        data_string = pickle.dumps(data_variable)
        replicatorSocketSender.send(data_string)
        logger.logWriter("Data sent to ReplicatorReciever", componentName)
    
    
conn.close()