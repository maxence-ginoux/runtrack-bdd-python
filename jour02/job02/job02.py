import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Root",
    database="laplateforme",
)
cursor = db.cursor()

cursor.execute (
    "CREATE TABLE etage ( id INT AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(255),numero INT,superficie INT)"
    
);

cursor.execute (
    "CREATE TABLE salle ( id INT AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(255),id_etage INT,capacite INT)"
    
);
