<<<<<<< HEAD
import mysql.connector
from datetime import datetime
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "12345",
    database = "readerDB"
)

myCursor = db.cursor()
=======
import sys
sys.path.append('../')
import mysql.connector
from datetime import datetime

db = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    passwd = "1969",
    database = "readerDB"
)
myCursor = db.cursor(buffered=True)
>>>>>>> Branislav
############################################### konektovanje na bazu

def AddToTable(value, code, database):
    now = datetime.now()

    #now = now.strftime("%H:%M:%S")
<<<<<<< HEAD
    myCursor.execute(f"INSERT INTO {database} (value, code, timeStamp) VALUES (%s, %s, %s)", (value,code,now))
    db.commit()
=======

    myCursor.execute(f"INSERT INTO {database} (value, code, timeStamp) VALUES (%s, %s, %s)", (value,code,now))
    db.commit()

>>>>>>> Branislav
def ReadFromTable(code1, code2, database):

    myCursor.execute(F"SELECT * FROM {database} WHERE code in ('{code1}', '{code2}') order by id desc")
    first = 1

    for x in myCursor:

        if(first == 1):
            data1 = x
            first = 0
<<<<<<< HEAD
            
        if(x[1] != data1[1]):
            data2 = x
            break

    
    return data1,data2
    

=======
            if(code2 == ""):
                return data1
            
        if(x[1] != data1[1]):
            data2 = x
            return data1,data2
    


def ReadHistorical(histociralValue,database):

    myCursor.execute(F"SELECT * FROM {database} WHERE code = '{histociralValue.code}' and (timeStamp >= '{histociralValue.fromTime}' and timeStamp <= '{histociralValue.toTime}')")

    retArray = []

    for x in myCursor:
        retArray.append(x)
    
    return retArray
        
>>>>>>> Branislav
