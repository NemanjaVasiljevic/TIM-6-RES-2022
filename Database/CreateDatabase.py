import mysql.connector

db = mysql.connector.connect(
    host = "127.0.0.1", #stavi localhost ili svoj ip vrv ce biti isti kao i ovaj proveri u MySql Workbench
    user = "root",
    passwd = "1969" #stavi svoju sifru
)

myCursor = db.cursor()
myCursor.execute("CREATE DATABASE readerDB")