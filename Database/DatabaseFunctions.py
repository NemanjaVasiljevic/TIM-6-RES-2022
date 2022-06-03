import mysql.connector
from datetime import datetime

db = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    passwd = "1969",
    database = "readerDB"
)

myCursor = db.cursor()
############################################### konektovanje na bazu

def AddToTable(value, code, database):
    now = datetime.now()

    #now = now.strftime("%H:%M:%S")

    myCursor.execute(f"INSERT INTO {database} (value, code, timeStamp) VALUES (%s, %s, %s)", (value,code,now))
    db.commit()

def ReadFromTable(code, database):
    data = []
    myCursor.execute(F"SELECT * FROM {database} WHERE code in ('{code}')")
    for x in myCursor:
        data.append(x)
    
    return data

