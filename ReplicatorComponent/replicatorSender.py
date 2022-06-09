import sys
sys.path.append('../')
import socket,pickle,time,random
from Model.DataModel import Data, Request





#Socket za primanje podataka od Writer komponente
writerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
writerSocket.bind((socket.gethostname(), 7000))
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
    if(data_variable.request == "WriteRequest"): 
        print(F"{data_variable.request,data_variable.data.value, data_variable.data.code}")
        # Pickle the object and send it to ReplicatorReciever
        data_string = pickle.dumps(data_variable)
        replicatorSocketSender.send(data_string)
        print("Uspesno poslao WriteRequest i podatke uz njega replikatoru")

    elif(data_variable.request == "ReadTable"):
        data_string = pickle.dumps(data_variable)
        replicatorSocketSender.send(data_string)
        print("Uspesno poslao ReadRequest i podatke uz njega replikatoru")


conn.close()