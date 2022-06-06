import sys
sys.path.append('../')
import socket,pickle,time,random
from Model.DataModel import Data





#Socket za primanje podataka od Writer komponente
writerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
writerSocket.bind((socket.gethostname(), 8000))
writerSocket.listen()

#Socket za komunikaciju sa ReplicatorReciever komponentom
replicatorSocketSender= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
replicatorSocketSender.connect((socket.gethostname(),10100))

print("Waiting for the Writer to send data...")
conn, addr = writerSocket.accept()
print('Connected by', addr)

while True:
    
    data = conn.recv(4096)
    data_variable = pickle.loads(data)
    print("Recieved from Writer:")
    
    if(type(data_variable) is Data):

        print(f"Code : {data_variable.code}   Value: {data_variable.value}")
        # Pickle the object and send it to ReplicatorReciever
        data_string = pickle.dumps(data_variable)
        replicatorSocketSender.send(data_string)
        print("Data sent to ReplicatorReciever")
    
    
conn.close()