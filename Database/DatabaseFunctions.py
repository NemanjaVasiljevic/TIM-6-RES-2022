import mysql.connector

db = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    passwd = "1969",
    database = "readerDB"
)

myCursor = db.cursor()
############################################### konektovanje na bazu

def AddToTable(value, code):
    myCursor.execute("INSERT INTO dataset1 (value, code) VALUES (%s, %s)", (value,code))
    db.commit()

def SeeTable():
    myCursor.execute("SELECT * FROM dataset1")
    for x in myCursor:
        print(x)
    

