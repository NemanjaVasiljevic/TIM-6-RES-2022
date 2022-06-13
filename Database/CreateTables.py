import mysql.connector

db = mysql.connector.connect(
<<<<<<< HEAD
    host = "localhost",
    user = "root",
    passwd = "12345",
=======
    host = "127.0.0.1",
    user = "root",
    passwd = "1969",
>>>>>>> Branislav
    database = "readerDB"
)

myCursor = db.cursor()

def CreateTables():
<<<<<<< HEAD
    
        myCursor.execute("CREATE TABLE DataSet1(value VARCHAR(50) NOT NULL, code VARCHAR(50) NOT NULL, id int PRIMARY KEY NOT NULL AUTO_INCREMENT, timeStamp DATETIME NOT NULL)")
        myCursor.execute("CREATE TABLE DataSet2(value VARCHAR(50) NOT NULL, code VARCHAR(50) NOT NULL, id int PRIMARY KEY NOT NULL AUTO_INCREMENT, timeStamp DATETIME NOT NULL)")
        myCursor.execute("CREATE TABLE DataSet3(value VARCHAR(50) NOT NULL, code VARCHAR(50) NOT NULL, id int PRIMARY KEY NOT NULL AUTO_INCREMENT, timeStamp DATETIME NOT NULL)")
        myCursor.execute("CREATE TABLE DataSet4(value VARCHAR(50) NOT NULL, code VARCHAR(50) NOT NULL, id int PRIMARY KEY NOT NULL AUTO_INCREMENT, timeStamp DATETIME NOT NULL)")

=======
    myCursor.execute("CREATE TABLE DataSet1(value VARCHAR(50) NOT NULL, code VARCHAR(50) NOT NULL, id int PRIMARY KEY NOT NULL AUTO_INCREMENT, timeStamp DATETIME NOT NULL)")
    myCursor.execute("CREATE TABLE DataSet2(value VARCHAR(50) NOT NULL, code VARCHAR(50) NOT NULL, id int PRIMARY KEY NOT NULL AUTO_INCREMENT, timeStamp DATETIME NOT NULL)")
    myCursor.execute("CREATE TABLE DataSet3(value VARCHAR(50) NOT NULL, code VARCHAR(50) NOT NULL, id int PRIMARY KEY NOT NULL AUTO_INCREMENT, timeStamp DATETIME NOT NULL)")
    myCursor.execute("CREATE TABLE DataSet4(value VARCHAR(50) NOT NULL, code VARCHAR(50) NOT NULL, id int PRIMARY KEY NOT NULL AUTO_INCREMENT, timeStamp DATETIME NOT NULL)")
>>>>>>> Branislav
