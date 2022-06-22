import sys
sys.path.append('../')
import socket,pickle,threading
from Logger.Logger import logWriter

class ClientThread(threading.Thread):
    def __init__(self,clientAddress,clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket

    def run(self):
        while True:
            data = conn.recv(4096)
            data_variable = pickle.loads(data)
            
            if(data_variable.request == "WriteRequest"): 
                data_string = pickle.dumps(data_variable)
                replicatorSocketSender.send(data_string)
                logWriter(f"Primio od WRITER ({data_variable.data}) saljem na REPLICATOR RECIVER","REPLICATOR SENDER")

            elif(data_variable.request == "ReadTable"):
                data_string = pickle.dumps(data_variable)
                replicatorSocketSender.send(data_string)
                logWriter(f"Primio od WRITER (ReadTable Request) saljem na REPLICATOR RECIVER","REPLICATOR SENDER")

            elif data_variable.request == "ReadHistorical":
                print("Dobio read request")
                data_string = pickle.dumps(data_variable)
                replicatorSocketSender.send(data_string)
                logWriter(f"Primio od WRITER (ReadHistorical Request) saljem na REPLICATOR RECIVER","REPLICATOR SENDER")



#Socket za primanje podataka od Writer komponente
writerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
writerSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
writerSocket.bind((socket.gethostname(), 7000))


#Socket za komunikaciju sa ReplicatorReciever komponentom
replicatorSocketSender= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
replicatorSocketSender.connect((socket.gethostname(),10100))


while True:

    writerSocket.listen()    
    conn, addr = writerSocket.accept()

    newThread = ClientThread(addr,conn)
    newThread.start()

