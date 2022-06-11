import sys
sys.path.append('../')
import socket,pickle,time,random
import os


gasi=False

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
      os.close("Writer.py")
      gasi==True
    elif(q1=="3"):
      dateFrom=input("Unesite datum od kada zelite da citate iz baze: ")
      dateTo=input("Unesite datum do kog zelite da citate iz baze: ")
    elif(q1=="4"):  
      print("Izaberite dva koda koje zelite da procitate iz baze:")
      print("1. CODE_ANALOG")
      print("2. CODE_DIGITAL")
      print("3. CODE_CUSTOM")
      print("4. CODE_LIMITSET")
      print("5. CODE_SINGLENOE")
      print("6. CODE_MULTIPLENODE")
      print("7. CODE_CONSUMER")
      print("8. CODE_SOURCE")
      kod1=input()
      kod2=input()