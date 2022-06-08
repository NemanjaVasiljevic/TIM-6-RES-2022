import sys
sys.path.append('../')
import socket,pickle
#from Database.CreateTables import CreateTables
from Model.DataModel import Data,Reader,Request,HistoricalValue


##### ovo se radi samo prvi put prilikom pokretanja posle samo zakomenterises
#CreateDatabase()
#CreateTables()
#############################################################################

'''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(),8000))
s.listen(1)
print("Waiting for connection...")

requestSocket, address = s.accept()
print(f"Connection established from address {address}")

request = requestSocket.recv(4098)
request = Request(pickle.loads(request))
'''

r1 = Reader(8001,"dataset1")
#clientSocket1 = r1.Connect()
r2 = Reader(8002,"dataset2")
#clientSocket2 = r1.Connect()
r3 = Reader(8003,"dataset3")
#clientSocket3 = r1.Connect()
r4 = Reader(8004,"dataset4")
#clientSocket4 = r1.Connect()



'''
while True:
    if(request.request == "WriteRequest"):
        r1.WriteData(clientSocket1,"dataset1")
     
    else:
        dataRead1, dataRead2 = r1.ReadData("CODE_DIGITAL", "CODE_ANALOG")
        dataRead1 = Data(dataRead1[0],dataRead1[1])
        dataRead2 = Data(dataRead2[0],dataRead2[1])
        print(F"Value 1 : {dataRead1.str()}\n Value 2: {dataRead2.str()}")
'''
val = HistoricalValue("CODE_DIGITAL","2022-06-04 13:15:49", "2022-06-04 13:16:09")
response = r1.ReadHistory(val)

for x in response:
    print(F"Value: {x[0]} Code: {x[1]}")





