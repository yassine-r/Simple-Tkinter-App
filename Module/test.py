import sqlite3

db_loc=sqlite3.connect('Insea.db')
cursor = db_loc.cursor()

cursor.execute('''SELECT idFiliere,nomFiliere FROM filiere;''')
rows= cursor.fetchall()
for row in rows:
    print(row)