import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "milan123",
    database = "res"
)

myCursor = db.cursor()

myCursor.execute("CREATE TABLE DataSet1(value VARCHAR(50) NOT NULL, code VARCHAR(50) NOT NULL, id int PRIMARY KEY NOT NULL AUTO_INCREMENT)")
myCursor.execute("CREATE TABLE DataSet2(value VARCHAR(50) NOT NULL, code VARCHAR(50) NOT NULL, id int PRIMARY KEY NOT NULL AUTO_INCREMENT)")
myCursor.execute("CREATE TABLE DataSet3(value VARCHAR(50) NOT NULL, code VARCHAR(50) NOT NULL, id int PRIMARY KEY NOT NULL AUTO_INCREMENT)")
myCursor.execute("CREATE TABLE DataSet4(value VARCHAR(50) NOT NULL, code VARCHAR(50) NOT NULL, id int PRIMARY KEY NOT NULL AUTO_INCREMENT)")
