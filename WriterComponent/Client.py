import sys
sys.path.append('../')
import socket,pickle,os,time
from Model.DataModel import Data, HistoricalValue,Request


def Menu():
    print("Izaberite neku od sledecih opcija:")
    print("1. Paljenje novog Writer-a")
    print("2. Gasenje Writer-a")
    print("3. Citanje iz baze po istoriji")
    print("4. Citanje iz baze po odredjenim kodovima")
    q1=input()
    
    try:
      broj = int(q1)
    except:
      return None
    
    if broj > 4 or broj <1:
          return None
    else:
          return q1

def SendHistoricalRequest(s):
      dateFrom=input("Unesite datum od kada zelite da citate iz baze: ")
      dateTo=input("Unesite datum do kog zelite da citate iz baze: ")
      print("Unesite neki od sledecih kodova: CODE_ANALOG,CODE_DIGITAL,CODE_CUSTOM,CODE_LIMITSET,CODE_SINGLENOE,CODE_MULTIPLENODE,CODE_CONSUMER,CODE_SOURCE")
      code=input()
      
      data = HistoricalValue(code,dateFrom,dateTo )
      request = Request("ReadHistorical",data)
      data_string = pickle.dumps(request)
      s.send(data_string)
  
def ReciveHistoricalRequest():
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
              
def SendCodeRequest(s):
      print("Izaberite dva koda koje zelite da procitate iz baze, kodovi su:CODE_ANALOG,CODE_DIGITAL,CODE_CUSTOM,CODE_LIMITSET,CODE_SINGLENOE,CODE_MULTIPLENODE,CODE_CONSUMER,CODE_SOURCE")
      kod1=input()
      kod2=input()
      data= Data(kod1,kod2)
      request=Request("ReadTable",data)
      data_string = pickle.dumps(request)
      s.send(data_string)
      
def ReciveCodeRequest():
      recived = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      recived.bind((socket.gethostname(),1234))
      recived.listen(1)

      readerSocket, address = recived.accept()

      msg = readerSocket.recv(4098)
      recivedMsg = pickle.loads(msg)

      print(F"{recivedMsg[0]}\n{recivedMsg[1]}")
      
def main():
      s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
      s.connect((socket.gethostname(),7000))
      
      while True:
        q1 = Menu()
        
        if(q1=="1"):
          os.system("start cmd /k python Writer.py")
          
        elif(q1=="2"):
          print("ugasilo se")
          
        elif(q1=="3"):
          SendHistoricalRequest(s)
          ReciveHistoricalRequest()
          
        elif(q1=="4"):  
          SendCodeRequest(s)
          ReciveCodeRequest()
     
if __name__ == '__main__':
        main()
