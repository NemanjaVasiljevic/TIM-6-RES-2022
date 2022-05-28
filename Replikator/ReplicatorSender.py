import socket 
import pickle


class Data:
    def __init__(self,code,value):
        self.code = code
        self.age = value

WriterSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
WriterSocket.bind((socket.gethostname(), 8081))
WriterSocket.listen()
print("Waiting for connections...")
conn, addr = WriterSocket.accept()
print('Connected by', addr)

while True:
    data = conn.recv(4096)
    data_variable = pickle.loads(data)
    
    print(data_variable.name)
    print(data_variable.age)
    # Access the information by doing data_variable.process_id or data_variable.task_id etc..,
    print ('Data received from client')
conn.close()    