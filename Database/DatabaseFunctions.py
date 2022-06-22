import sys
from mysqlx import DatabaseError
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
    try:
        myCursor = db.cursor()
        now = datetime.now()

        myCursor.execute(f"INSERT INTO {database} (value, code, timeStamp) VALUES (%s, %s, %s)", (value,code,now))
        db.commit()
    except DatabaseError:
        return DatabaseError

def ReadFromTable(code1, database,db):

    try:
        myCursor = db.cursor(buffered=True)
        
        myCursor.execute(F"SELECT * FROM {database} WHERE code = '{code1}' order by id desc")
        for x in myCursor:
            data1 = x
            return data1
    except DatabaseError:
        return DatabaseError



def ReadHistorical(histociralValue,database,db):

    try:
        myCursor = db.cursor()
        myCursor.execute(F"SELECT * FROM {database} WHERE code = '{histociralValue.code}' and (timeStamp >= '{histociralValue.fromTime}' and timeStamp <= '{histociralValue.toTime}')")
        retArray = []

        for x in myCursor:
            retArray.append(x)
        
        return retArray
    except DatabaseError:
        return DatabaseError


        
