import mysql.connector

db = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    passwd = "1969",
    database = "readerDB"
)

myCursor = db.cursor()

def CreateTables():
    myCursor.execute("CREATE TABLE DataSet1(value VARCHAR(50) NOT NULL, code VARCHAR(50) NOT NULL, id int PRIMARY KEY NOT NULL AUTO_INCREMENT, timeStamp DATETIME NOT NULL)")
    myCursor.execute("CREATE TABLE DataSet2(value VARCHAR(50) NOT NULL, code VARCHAR(50) NOT NULL, id int PRIMARY KEY NOT NULL AUTO_INCREMENT, timeStamp DATETIME NOT NULL)")
    myCursor.execute("CREATE TABLE DataSet3(value VARCHAR(50) NOT NULL, code VARCHAR(50) NOT NULL, id int PRIMARY KEY NOT NULL AUTO_INCREMENT, timeStamp DATETIME NOT NULL)")
    myCursor.execute("CREATE TABLE DataSet4(value VARCHAR(50) NOT NULL, code VARCHAR(50) NOT NULL, id int PRIMARY KEY NOT NULL AUTO_INCREMENT, timeStamp DATETIME NOT NULL)")
