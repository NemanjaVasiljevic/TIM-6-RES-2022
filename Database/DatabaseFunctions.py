import mysql.connector

db = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    passwd = "1969",
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
    

