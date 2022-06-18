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
############################################### konektovanje na bazu

def AddToTable(value, code, database):
    now = datetime.now()

    try:
        myCursor.execute(f"INSERT INTO {database} (value, code, timeStamp) VALUES (%s, %s, %s)", (value,code,now))
        db.commit()
        return 0;
    except:
        return -1;

def ReadFromTable(code1, code2, database):

    try:
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
    except:
        return -1
    


def ReadHistorical(histociralValue,database):

    myCursor.execute(F"SELECT * FROM {database} WHERE code = '{histociralValue.code}' and (timeStamp >= '{histociralValue.fromTime}' and timeStamp <= '{histociralValue.toTime}')")

    retArray = []

    for x in myCursor:
        retArray.append(x)
    
    return retArray
        
