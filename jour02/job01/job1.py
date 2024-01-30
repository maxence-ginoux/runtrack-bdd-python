
import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Root",
    database="laplateforme",
)

cursor = db.cursor()

cursor.execute("SELECT * FROM etudiant")

etudiant = cursor.fetchall()
print(etudiant)

