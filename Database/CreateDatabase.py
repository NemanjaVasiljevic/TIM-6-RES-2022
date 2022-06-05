import mysql.connector

db = mysql.connector.connect(
    host = "localhost", #stavi localhost ili svoj ip vrv ce biti isti kao i ovaj proveri u MySql Workbench
    user = "root",
    passwd = "milan123" #stavi svoju sifru
)

print(db)
mycursor = db.cursor()