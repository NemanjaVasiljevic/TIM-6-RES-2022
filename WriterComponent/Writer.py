import sys
sys.path.append('../')
import socket,pickle,time,random
from Model.DataModel import Data, HistoricalValue,Request
listNames = ["CODE_ANALOG","CODE_DIGITAL","CODE_CUSTOM","CODE_LIMITSET","CODE_SINGLENOE","CODE_MULTIPLENODE","CODE_CONSUMER","CODE_SOURCE"]

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),7000))

option = 2

while True:

    if option == 1:
        time.sleep(2)
        data = Data(random.randint(1,500),random.choice(listNames))
        request = Request("WriteRequest",data)


        data_string = pickle.dumps(request)
        s.send(data_string)
        print("Sending to ReplicatorSender:")
        print(f"Code : {request.data.code}   Value: {request.data.value}")

    elif option == 2:
        print("Dobio read request")
        data = HistoricalValue("CODE_ANALOG","2022-06-10 19:49:53", "2022-06-10 19:50:33")
        request = Request("ReadHistorical",data)
        data_string = pickle.dumps(request)
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