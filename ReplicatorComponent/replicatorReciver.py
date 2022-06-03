import sys
sys.path.append('../')
import socket,pickle,time,random
from Model.DataModel import Data




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





while True:
    
    # Create an instance of Person to send to server.
    #variable = Data(random.choice(listNames),random.randint(1,500))
    # Pickle the object and send it to the server
    #data_string = pickle.dumps(variable)
    #readerSocket.send(data_string)

    data = conn.recv(4096)
    data_variable = pickle.loads(data)
    print("Recieved from ReplicatorSender:")
    print(f"Code : {data_variable.code}   Value: {data_variable.value}")
    print("Data Sent to Reader component...")
    data_string = pickle.dumps(data_variable)
    readerSocket.send(data_string)
    
    

client.close()