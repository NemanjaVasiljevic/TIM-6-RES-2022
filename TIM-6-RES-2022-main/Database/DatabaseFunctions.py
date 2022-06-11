import mysql.connector
from datetime import datetime
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "12345",
    database = "readerDB"
)

myCursor = db.cursor()
############################################### konektovanje na bazu

def AddToTable(value, code, database):
    now = datetime.now()

    #now = now.strftime("%H:%M:%S")
    myCursor.execute(f"INSERT INTO {database} (value, code, timeStamp) VALUES (%s, %s, %s)", (value,code,now))
    db.commit()
def ReadFromTable(code1, code2, database):

    myCursor.execute(F"SELECT * FROM {database} WHERE code in ('{code1}', '{code2}') order by id desc")
    first = 1

    for x in myCursor:

        if(first == 1):
            data1 = x
            first = 0
            
        if(x[1] != data1[1]):
            data2 = x
            break

    
    return data1,data2
    

