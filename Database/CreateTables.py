import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "12345",
    database = "readerDB"
)

myCursor = db.cursor()

def CreateTables():
    
        myCursor.execute("CREATE TABLE DataSet1(value VARCHAR(50) NOT NULL, code VARCHAR(50) NOT NULL, id int PRIMARY KEY NOT NULL AUTO_INCREMENT, timeStamp DATETIME NOT NULL)")
        myCursor.execute("CREATE TABLE DataSet2(value VARCHAR(50) NOT NULL, code VARCHAR(50) NOT NULL, id int PRIMARY KEY NOT NULL AUTO_INCREMENT, timeStamp DATETIME NOT NULL)")
        myCursor.execute("CREATE TABLE DataSet3(value VARCHAR(50) NOT NULL, code VARCHAR(50) NOT NULL, id int PRIMARY KEY NOT NULL AUTO_INCREMENT, timeStamp DATETIME NOT NULL)")
        myCursor.execute("CREATE TABLE DataSet4(value VARCHAR(50) NOT NULL, code VARCHAR(50) NOT NULL, id int PRIMARY KEY NOT NULL AUTO_INCREMENT, timeStamp DATETIME NOT NULL)")

