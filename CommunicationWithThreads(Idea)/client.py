import socket
import os
import random
import time
import threading
from multiprocessing import Process 
SERVER = "127.0.0.1"
PORT = 8082
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))
client.sendall(bytes("This is from Client",'UTF-8'))




def Send(client,list):
  b = None
  while b is None:
    time.sleep(2)
    client.sendall(bytes(random.choice(list),'UTF-8'))
    
  

def Console():
 
   print("1.Pokreni novog klijenta")
   print("2.Obustavi konekciju")
   a = input()

   if a == '1':
    os.system("start cmd /k py client.py")
   
   elif a == '2':
        
        print("Unesite poruku \"bye\"da prekinete konekciju") 
        out_data = input()
        client.sendall(bytes(out_data,'UTF-8'))
        
        client.close()
        print("Client has closed")
        exit(1)




  



list = ["A","B","C"]

while True:

      
      p1 = Process(target = Console())
      p1.start()
      p2 =Process(target=Send(client,list))
      p2.start()     
      
      
  
    
  
 

  
  

  
         


  
client.close()