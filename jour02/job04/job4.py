import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Root",
    database="laplateforme",
)
cursor = db.cursor()