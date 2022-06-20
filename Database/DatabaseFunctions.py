import sys
sys.path.append('../')
import mysql.connector
from datetime import datetime

def ConnectDatabase():

    db = mysql.connector.connect(
        host = "127.0.0.1",
        user = "root",
        passwd = "1969",
        database = "readerDB"
    )    
    return db
        
############################################### konektovanje na bazu

def AddToTable(value, code, database,db):
    myCursor = db.cursor()
    now = datetime.now()

    myCursor.execute(f"INSERT INTO {database} (value, code, timeStamp) VALUES (%s, %s, %s)", (value,code,now))
    db.commit()


def ReadFromTable(code1, code2, database,db):

    myCursor = db.cursor()
    
    myCursor.execute(F"SELECT * FROM {database} WHERE code in ('{code1}', '{code2}') order by id desc")
    first = 1
    for x in myCursor:

        if(first == 1):
            data1 = x
            first = 0
            if(code2 == ""):
                return data1
            
        if(x[1] != data1[1]):
            data2 = x
            return data1,data2
    


def ReadHistorical(histociralValue,database,db):

    myCursor = db.cursor
    myCursor.execute(F"SELECT * FROM {database} WHERE code = '{histociralValue.code}' and (timeStamp >= '{histociralValue.fromTime}' and timeStamp <= '{histociralValue.toTime}')")
    retArray = []

    for x in myCursor:
        retArray.append(x)
    
    return retArray


        
