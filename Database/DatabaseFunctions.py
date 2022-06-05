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

def SeeTable():
    myCursor.execute("SELECT * FROM dataset1")
    for x in myCursor:
        print(x)
    

