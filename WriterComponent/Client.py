import sys
sys.path.append('../')
import socket,pickle,os
from Model.DataModel import Data, HistoricalValue,Request

gasi=False
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),2000))
while(True):
    print("Izaberite neku od sledecih opcija:")
    print("1. Paljenje novog Writer-a")
    print("2. Gasenje Writer-a")
    print("3. Citanje iz baze po istoriji")
    print("4. Citanje iz baze po odredjenim kodovima")
    q1=input()
    if(q1=="1"):  
      os.system("start cmd /k python Writer.py")
    elif(q1=="2"):
      request = Request("CloseWriter",data)
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
    elif(q1=="4"):  
      print("Izaberite dva koda koje zelite da procitate iz baze, kodovi su:CODE_ANALOG,CODE_DIGITAL,CODE_CUSTOM,CODE_LIMITSET,CODE_SINGLENOE,CODE_MULTIPLENODE,CODE_CONSUMER,CODE_SOURCE")
      kod1=input()
      kod2=input()
    else:   
      request = Request("WriteRequest",data)
      data_string = pickle.dumps(request)
      s.send(data_string)