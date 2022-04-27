import sqlite3
from tkinter import *
import tkinter.messagebox
import Module.tools
from tkinter.ttk import *
import Module.filiere

db_loc=sqlite3.connect('Insea.db')
cursor = db_loc.cursor()

def Etudiantlist():
    lst=[]
    cursor.execute('''SELECT * FROM Etudiant;''')
    rows = cursor.fetchall()
    for row in rows:
        lst.append(row)
    return lst
def lastidStudent():
    lst=[]
    cursor.execute('''SELECT idEtudiant FROM Etudiant;''')
    rows=cursor.fetchall()
    for row in rows:
        lst.append(row)
    return lst[-1][0]

def addStudent(window,idEtudiant,Nom,Prenom,idFiliere,Age):
    window.attributes('-topmost',True)
    a=0
    l=[str(idEtudiant),str(Nom),str(Prenom),str(idFiliere),str(Age)]
    for i in l:
        if i=="":
            a=1
    if a==0:
        i=0
        for row in Etudiantlist():
            if str(row[0])==str(idEtudiant):
                i=1
        if(i==0):
            cursor.execute('''INSERT INTO Etudiant VALUES (?,?,?,?,?);''', (idEtudiant,int(idFiliere),str(Nom),str(Prenom),int(Age)))
            db_loc.commit()
            tkinter.messagebox.showinfo("Message", "l'étudiant est bien ajouté \n (merci de cliquer sur actualiser pour voir le changement)")
        else:
            tkinter.messagebox.showinfo("Message", "id existant, essayez un autre id")
    else:
        tkinter.messagebox.showinfo("Message", "rempli toutes les cases !")
def modifyStudent(idEtudiant,Nom,Prenom,idFiliere,Age):
    a=0
    l=[idEtudiant,Nom,Prenom,idFiliere,Age]
    for i in l:
        if i=="":
            a=1
    if a==0:
        cursor.execute('''UPDATE Etudiant SET Nom=?,Prenom=?,IdFiliereFK=?,Age=? WHERE idEtudiant=?;''', (Nom,Prenom,int(idFiliere),Age,idEtudiant))
        db_loc.commit()
        tkinter.messagebox.showinfo("Message", "la modification est bien faite \n (merci de cliquer sur actualiser pour voir le changement)")

def removeStudent(idEtudiant):
    if idEtudiant!="":
        cursor.execute('''DELETE FROM Etudiant WHERE idEtudiant={};'''.format(idEtudiant))
        db_loc.commit()

def Studentsliste():
    lst=[]
    cursor.execute('''SELECT * FROM Etudiant;''')
    rows = cursor.fetchall()
    for row in rows:
        lst.append(row)
    return lst

def getStudent(idEtudiant):
    lst=[]
    cursor.execute('''SELECT Nom,Prenom,idFiliere,Age FROM filiere WHERE idEtudiant={};'''.format(idEtudiant))
    row= cursor.fetchone()
    return row

def ShowStudents(window):
    i=0
    for row in Studentsliste():
        window.insert(i,str(row[0])+" - "+str(Module.filiere.getFiliere(int(row[1])))+" - "+str(row[2])+" - "+str(row[3])+" - "+str(row[4]))
        i=i+1

def Insertion(window):
    newWindow =Toplevel(window)
    newWindow.attributes('-topmost',True)
    newWindow.title("Ajout d'un étudiant")
    tkinter.Label(newWindow, text="id:").grid(row=0, column=0, padx=15, pady=15)
    tkinter.Label(newWindow, text="Prenom:").grid(row=1, column=0, padx=15, pady=15)
    tkinter.Label(newWindow, text="Nom:").grid(row=2, column=0, padx=15, pady=15)
    tkinter.Label(newWindow, text="Filiere:").grid(row=3, column=0, padx=15, pady=15)
    tkinter.Label(newWindow, text="Age:").grid(row=4, column=0, padx=15, pady=15)

    my_va2r= StringVar(newWindow)
    my_va2r.set("0")
    en0 = Spinbox(newWindow, from_= 0,to = 9999999999,textvariable=my_va2r)  
    en0['state'] = 'readonly'
    en1 = tkinter.Entry(newWindow)
    en2 = tkinter.Entry(newWindow)
    n = tkinter.StringVar()
    en3 =Combobox(newWindow,textvariable = n)
    en3['state'] = 'readonly'
    en3['values']=tuple(Module.filiere.getFilieres())
    if Module.filiere.getFilieres()!=[]:
        en3.current(0)
    my_var= StringVar(newWindow)
    my_var.set("18")
    en4 = Spinbox(newWindow, from_= 0, to = 120,textvariable=my_var)
    en4['state'] = 'readonly'
    bt1 = tkinter.Button(newWindow, text="Enregistrer",bg="#85929E",fg="white",activebackground="#85929E",relief="ridge")

    en0.grid(row=0, column=1, padx=5, pady=5)
    en1.grid(row=1, column=1, padx=5, pady=5)
    en2.grid(row=2, column=1, padx=5, pady=5)
    en3.grid(row=3, column=1, padx=5, pady=5)
    en4.grid(row=4, column=1, padx=5, pady=5)
    bt1.grid(row=6, column=0,columnspan=2, padx=15, pady=15)

    bt1.config(command=lambda: addStudent(newWindow,en0.get(),en2.get(),en1.get(),Module.filiere.getid(en3.get()),en4.get()))
    newWindow.mainloop()

def suppression(window):
    if(Module.tools.selected_item(window)!=['']):
        result = tkinter.messagebox.askquestion("Message", "Êtes-vous sûr de vouloir supprimer l'étudiant : "+Module.tools.selected_item(window)[2]+"  "+Module.tools.selected_item(window)[3], icon='warning')
        if result == 'yes':
            removeStudent(int(Module.tools.selected_item(window)[0]))
            tkinter.messagebox.showinfo("Message", "l'étudiant "+Module.tools.selected_item(window)[2]+"  "+Module.tools.selected_item(window)[3]+" est bien retiré \n (merci de cliquer sur actualiser pour voir le changement)")
    else:
        result = tkinter.messagebox.showinfo("Message", "sélectionnez d'abord l'élève que vous voulez supprimer  ", icon='warning')

def modification(window,fil):
    if(Module.tools.selected_item(fil)!=['']):
        x=Module.tools.selected_item(fil)[0]
        newWindow =Toplevel(window)
        newWindow.attributes('-topmost',True)
        newWindow.title("Modification d'un étudiant")
        tkinter.Label(newWindow, text="le nouveau Nom:").grid(row=0, column=0, padx=15, pady=15)
        en1 = tkinter.Entry(newWindow)
        en1.insert(0, Module.tools.selected_item(fil)[2])
        en1.grid(row=0, column=1, padx=5, pady=5)
        tkinter.Label(newWindow, text="le nouveau Prenom:").grid(row=1, column=0, padx=15, pady=15)
        en2 = tkinter.Entry(newWindow)
        en2.insert(0, Module.tools.selected_item(fil)[3])
        en2.grid(row=1, column=1, padx=5, pady=5)

        tkinter.Label(newWindow, text="la nouvelle filière:").grid(row=2, column=0, padx=15, pady=15)
        n = tkinter.StringVar()
        en3 =Combobox(newWindow,textvariable = n)
        en3['state'] = 'readonly'
        en3['values']=tuple(Module.filiere.getFilieres())
        en3.current(0)
        en3.grid(row=2, column=1, padx=5, pady=5)

        tkinter.Label(newWindow, text="le nouveau Age:").grid(row=3, column=0, padx=15, pady=15)
        my_var= StringVar(newWindow)
        my_var.set("18")
        en4 = Spinbox(newWindow, from_= 0, to = 120,textvariable=my_var)
        en4['state'] = 'readonly'
        en4.grid(row=3, column=1, padx=5, pady=5)
        

        bt1 = tkinter.Button(newWindow, text="Enregistrer",bg="#85929E",fg="white",activebackground="#85929E",relief="ridge")
        bt1.grid(row=4, column=0,columnspan=2, padx=15, pady=15)
        bt1.config(command=lambda: modifyStudent(int(x),en1.get(),en2.get(),Module.filiere.getid(en3.get()),en4.get()))
    else:
        result = tkinter.messagebox.showinfo("Message", "sélectionnez d'abord l'élève que vous voulez modifier  ", icon='warning')
