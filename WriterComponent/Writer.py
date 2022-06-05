import sys
sys.path.append('../')
import socket,pickle,time,random
from Model.DataModel import Data
listNames = ["CODE_ANALOG","CODE_DIGITAL","CODE_CUSTOM","CODE_LIMITSET","CODE_SINGLENOE","CODE_MULTIPLENODE","CODE_CONSUMER","CODE_SOURCE"]

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),8000))
while True:
    time.sleep(2)
    variable = Data(random.randint(1,500),random.choice(listNames))
    data_string = pickle.dumps(variable)
    s.send(data_string)
    print("Sending to ReplicatorSender:")
    print(f"Code : {variable.code}   Value: {variable.value}")
