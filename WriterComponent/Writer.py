import sys
sys.path.append('../')
import socket,pickle,time,random,os,signal
import subprocess as kill
from Logger.Logger import logWriter
from Model.DataModel import Data, HistoricalValue,Request
listNames = ["CODE_ANALOG","CODE_DIGITAL","CODE_CUSTOM","CODE_LIMITSET","CODE_SINGLENOE","CODE_MULTIPLENODE","CODE_CONSUMER","CODE_SOURCE"]

#konktovanje na replicatorSender


def SocketConnect():
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((socket.gethostname(),7000))
    
    return s

def SendData(s):
    time.sleep(2)
    data = Data(random.randint(1,100),random.choice(listNames))
    request = Request("WriteRequest",data)
    data_string = pickle.dumps(request)
    s.send(data_string)
    logWriter(f"Writer poslao podatak na upis({data})","WRITER")  
         

def main():
    s = SocketConnect()
    while True:
        SendData(s)

if __name__ == '__main__':
        main()