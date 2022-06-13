import sys
sys.path.append('../')
import socket,pickle,os,time
from Model.DataModel import Data, HistoricalValue,Request

gasi=False
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

while(True):
    print("Izaberite neku od sledecih opcija:")
    print("1. Paljenje novog Writer-a")
    print("2. Gasenje Writer-a")
    print("3. Citanje iz baze po istoriji")
    print("4. Citanje iz baze po odredjenim kodovima")

    q1=input()
    
    if(q1=="1"):

      os.system("start cmd /k python Writer.py")
      s.connect((socket.gethostname(),2000)) 
      request = Request("WriteRequest","")
      data_string = pickle.dumps(request)
      s.send(data_string) 

    elif(q1=="2"):

     
      request = Request("CloseWriter","")
      data_string = pickle.dumps(request)
      s.send(data_string)

    elif(q1=="3"):

      dateFrom=input("Unesite datum od kada zelite da citate iz baze: ")
      dateTo=input("Unesite datum do kog zelite da citate iz baze: ")
      print("Unesite neki od sledecih kodova: CODE_ANALOG,CODE_DIGITAL,CODE_CUSTOM,CODE_LIMITSET,CODE_SINGLENOE,CODE_MULTIPLENODE,CODE_CONSUMER,CODE_SOURCE")
      code=input()
      
      data = HistoricalValue(code,dateFrom,dateTo )
      request = Request("ReadHistorical",data)
      data_string = pickle.dumps(request)
      s.send(data_string)

      recived = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      recived.bind((socket.gethostname(),1234))
      recived.listen(1)
      print("Waiting for connection...")

      readerSocket, address = recived.accept()
      print(f"Connection established from address {address}")

      msg = readerSocket.recv(4098)
      recivedMsg = pickle.loads(msg)

      for x in recivedMsg:
            tempData = Data(x[0],x[1])
            print(tempData)

      time.sleep(10)

    elif(q1=="4"):  
      print("Izaberite dva koda koje zelite da procitate iz baze, kodovi su:CODE_ANALOG,CODE_DIGITAL,CODE_CUSTOM,CODE_LIMITSET,CODE_SINGLENOE,CODE_MULTIPLENODE,CODE_CONSUMER,CODE_SOURCE")
      kod1=input()
      kod2=input()
