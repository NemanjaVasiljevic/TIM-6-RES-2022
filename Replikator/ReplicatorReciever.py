import socket,pickle,time,random



class Data:
    def __init__(self,code,value):
        self.code = code
        self.age = value

#1.	CODE_ANALOG
#2.	CODE_DIGITAL
#3.	CODE_CUSTOM
#4.	CODE_LIMITSET
#5.	CODE_SINGLENOE
#6.	CODE_MULTIPLENODE
#7.	CODE_CONSUMER
#8.	CODE_SOURCE


listNames = ["CODE_ANALOG","CODE_DIGITAL","CODE_CUSTOM","CODE_LIMITSET","CODE_SINGLENOE","CODE_MULTIPLENODE","CODE_CONSUMER","CODE_SOURCE"]

# Create a socket connection.
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((socket.gethostname(), 8081))


while True:
    
    # Create an instance of Person to send to server.
    variable = Data(random.choice(listNames),random.randint(1,500))
    # Pickle the object and send it to the server
    data_string = pickle.dumps(variable)
    client.send(data_string)


    print('Data Sent to Server')
    

client.close()