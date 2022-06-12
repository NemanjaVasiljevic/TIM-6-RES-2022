import sys
sys.path.append('../')
import socket,pickle,time,random,os
from Model.DataModel import Data, HistoricalValue,Request
listNames = ["CODE_ANALOG","CODE_DIGITAL","CODE_CUSTOM","CODE_LIMITSET","CODE_SINGLENOE","CODE_MULTIPLENODE","CODE_CONSUMER","CODE_SOURCE"]

#konktovanje na replicatorSender
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),7000))

#Soket za komunikaciju sa klijentom
sClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
sClient.bind((socket.gethostname(),2000))
sClient.listen(1)
SocketClient, addressClient = s.accept()
option = 1

while True:
    
    msgClient = SocketClient.recv(4098)
    recivedClient = pickle.loads(msgClient)


    if recivedClient.request == "ReadHistorical":
        print("Dobio read request")
        
        s.send(data_string)
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((socket.gethostname(),1234))
        s.listen(1)
        print("Waiting for connection...")

        readerSocket, address = s.accept()
        print(f"Connection established from address {address}")

        msg = readerSocket.recv(4098)
        recived = pickle.loads(msg)

        for x in recived:
            tempData = Data(x[0],x[1])
            print(tempData)

        option = 1
        time.sleep(10)

    elif recivedClient.request=="WriteRequest":
        time.sleep(2)
        data = Data(random.randint(1,500),random.choice(listNames))
        request = Request("WriteRequest",data)
        data_string = pickle.dumps(request)
        s.send(data_string)
        print("Sending to ReplicatorSender:")
        print(f"Code : {request.data.code}   Value: {request.data.value}")    
    elif recivedClient.request=="CloseWriter":
        os.close()