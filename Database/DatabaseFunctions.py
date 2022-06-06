import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "12345",
    database = "readerDB"
)

myCursor = db.cursor()
############################################### konektovanje na bazu

def AddToTable(value, code, database):
    myCursor.execute(f"INSERT INTO {database} (value, code) VALUES (%s, %s)", (value,code))
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
    

