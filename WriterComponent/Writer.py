import sys
sys.path.append('../')
import socket,pickle,time,random,os,signal
import subprocess as kill
from Model.DataModel import Data, HistoricalValue,Request
listNames = ["CODE_ANALOG","CODE_DIGITAL","CODE_CUSTOM","CODE_LIMITSET","CODE_SINGLENOE","CODE_MULTIPLENODE","CODE_CONSUMER","CODE_SOURCE"]

#konktovanje na replicatorSender
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),7000))



while True:
    time.sleep(2)
    data = Data(random.randint(1,100),random.choice(listNames))
    request = Request("WriteRequest",data)
    data_string = pickle.dumps(request)
    s.send(data_string)
    print("Sending to ReplicatorSender:")
    print(f"Code : {request.data.code}   Value: {request.data.value}")    
         