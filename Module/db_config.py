import sqlite3
db_loc=sqlite3.connect('Insea.db')
cursor = db_loc.cursor()

def createTables():

    cursor.execute('''CREATE TABLE filiere(
    idFiliere INTEGER PRIMARY KEY,
    nomFiliere TEXT);''')
    db_loc.commit()

    cursor.execute('''INSERT INTO filiere (idFiliere,nomFiliere) VALUES (1,'DSE');''')
    db_loc.commit()
    cursor.execute('''INSERT INTO filiere (idFiliere,nomFiliere) VALUES (2,'DS');''')
    db_loc.commit()
    cursor.execute('''INSERT INTO filiere (idFiliere,nomFiliere) VALUES (3,'AF');''')
    db_loc.commit()
    cursor.execute('''INSERT INTO filiere (idFiliere,nomFiliere) VALUES (4,'ROAD');''')
    db_loc.commit()

    cursor.execute('''CREATE TABLE Etudiant(
    idEtudiant INTEGER PRIMARY KEY,
    IdFiliereFK INTEGER,
    nom TEXT,
    prenom TEXT,
    age INTEGER,
    FOREIGN KEY(IdFiliereFK) REFERENCES filiere(idFiliere));''')
    db_loc.commit()

    cursor.execute('''INSERT INTO Etudiant (idEtudiant,IdFiliereFK,nom,prenom,age) VALUES (1,1,'rachidy','yassine',20);''')
    db_loc.commit()
    cursor.execute('''INSERT INTO Etudiant (idEtudiant,IdFiliereFK,nom,prenom,age) VALUES (2,2,'salhi','youssef',20);''')
    db_loc.commit()


def ajoutStudent(idEtudiant,Nom,Prenom,idFiliere,Age):
    cursor.execute('''INSERT INTO Etudiant VALUES (?,?,?,?,?);''', (idEtudiant,Nom,Prenom,idFiliere,Age))
    db_loc.commit()

def ajoutFiliere(idFiliere,nomFiliere):
    cursor.execute('''INSERT INTO filiere VALUES (?,?);''', (idFiliere,nomFiliere))
    db_loc.commit()


def modifyStudent(idEtudiant,Nom,Prenom,idFiliere,Age):
    cursor.execute('''UPDATE Etudiant SET Nom=?,Prenom=?,idFiliere=?,Age=? WHERE idEtudiant=?;''', (Nom,Prenom,idFiliere,Age,idEtudiant))
    db_loc.commit()

def modifyFiliere(idFiliere,nomFiliere):
    cursor.execute('''UPDATE filiere SET nomFiliere=? WHERE idFiliere=?;''', (idFiliere,nomFiliere))
    db_loc.commit()


def removeStudent(idEtudiant):
    cursor.execute('''DELETE FROM Etudiant WHERE idEtudiant=?;''', (idEtudiant))
    db_loc.commit()

def removeFiliere(idFiliere):
    cursor.execute('''DELETE FROM filiere WHERE idFiliere=?;''', (idFiliere))
    db_loc.commit()

if __name__ == '__main__':
    createTables()