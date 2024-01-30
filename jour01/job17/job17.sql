modifier l'âge de Betty Spaghetti en 20ans:
UPDATE etudiant SET age = 20 WHERE prenom = "Spaghetti" AND nom = "Betty";

vérifier que la modification a été effectuée:
SELECT * FROM etudiant WHERE prenom = "Spaghetti" AND nom = "Betty";