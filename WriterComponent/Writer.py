import sys
sys.path.append('../')
<<<<<<< HEAD
import socket,pickle,time,random
from Model.DataModel import Data
listNames = ["CODE_ANALOG","CODE_DIGITAL","CODE_CUSTOM","CODE_LIMITSET","CODE_SINGLENOE","CODE_MULTIPLENODE","CODE_CONSUMER","CODE_SOURCE"]

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),8000))
while True:
    time.sleep(2)
    variable = Data(random.randint(1,500),random.choice(listNames))
    data_string = pickle.dumps(variable)
    s.send(data_string)
    print("Sending to ReplicatorSender:")
    print(f"Code : {variable.code}   Value: {variable.value}")
=======
import socket,pickle,time,random,os,signal
import subprocess as kill
from Model.DataModel import Data, HistoricalValue,Request
listNames = ["CODE_ANALOG","CODE_DIGITAL","CODE_CUSTOM","CODE_LIMITSET","CODE_SINGLENOE","CODE_MULTIPLENODE","CODE_CONSUMER","CODE_SOURCE"]

#konktovanje na replicatorSender
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),7000))

#Soket za komunikaciju sa klijentom
sClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
sClient.bind((socket.gethostname(),2000))
    
sClient.listen(1)
SocketClient, addressClient = sClient.accept()

while True:

    print("Upao u while prosao connect")
    
    msgClient = SocketClient.recv(4098)
    recivedClient = pickle.loads(msgClient)


    print("Primio")

    if recivedClient.request == "ReadHistorical":


        print("Dobio read request")      
        s.send(msgClient)

 
    elif recivedClient.request=="CloseWriter":
       pid = os.getpid()
       kill.Popen('taskkill /F /PID {0}'.format(pid), shell=True)
        
    elif recivedClient.request == "WriteRequest":       
        time.sleep(2)
        data = Data(random.randint(1,100),random.choice(listNames))
        request = Request("WriteRequest",data)
        data_string = pickle.dumps(request)
        s.send(data_string)
        print("Sending to ReplicatorSender:")
        print(f"Code : {request.data.code}   Value: {request.data.value}")   
>>>>>>> Branislav
