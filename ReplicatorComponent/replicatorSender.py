import sys
sys.path.append('../')
import socket,pickle,threading
from Model.DataModel import Data, Request

class ClientThread(threading.Thread):
    def __init__(self,clientAddress,clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print ("New connection added: ", clientAddress)

    def run(self):
        while True:
            data = conn.recv(4096)
            data_variable = pickle.loads(data)
            
            if(data_variable.request == "WriteRequest"): 
                data_string = pickle.dumps(data_variable)
                replicatorSocketSender.send(data_string)
                print("Uspesno poslao WriteRequest i podatke uz njega replikatorReciveru")

            elif(data_variable.request == "ReadTable"):
                data_string = pickle.dumps(data_variable)
                replicatorSocketSender.send(data_string)
                print("Uspesno poslao ReadRequest i podatke uz njega replikatoru")

            elif data_variable.request == "ReadHistorical":
                print("Dobio read request")
                data_string = pickle.dumps(data_variable)
                replicatorSocketSender.send(data_string)


#server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)



#Socket za primanje podataka od Writer komponente
writerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
writerSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
writerSocket.bind((socket.gethostname(), 7000))


#Socket za komunikaciju sa ReplicatorReciever komponentom
replicatorSocketSender= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
replicatorSocketSender.connect((socket.gethostname(),10100))

print("Waiting for the Writer to send data...")


while True:

    writerSocket.listen()    
    conn, addr = writerSocket.accept()

    newThread = ClientThread(addr,conn)
    newThread.start()

conn.close()