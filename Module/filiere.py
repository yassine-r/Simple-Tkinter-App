import sqlite3
from tkinter import *
import tkinter.messagebox
import Module.tools


db_loc=sqlite3.connect('Insea.db')
cursor = db_loc.cursor()


def addFiliere(window,idFiliere,nomFiliere):
    window.attributes('-topmost',True)
    if str(nomFiliere)=="" or str(idFiliere)=="":
        tkinter.messagebox.showinfo("Message", "rempli toutes les cases !")
    else:
        i=0
        for row in Filiereslist():
            if str(row[0])==str(idFiliere):
                i=1
        if(i==0):
            cursor.execute('''INSERT INTO filiere VALUES (?,?);''', (int(idFiliere),nomFiliere))
            db_loc.commit()
            tkinter.messagebox.showinfo("Message", "la nouvelle filiere est bien ajoutée\n(merci de cliquer sur actualiser pour voir le changement)")
        else:
            tkinter.messagebox.showinfo("Message", "id existant, essayez un autre id")
def modifyFiliere(idFiliere1,nomFiliere):
    if nomFiliere!="":
        cursor.execute('''UPDATE filiere SET nomFiliere=? WHERE idFiliere=?;''', (nomFiliere,idFiliere1))
        db_loc.commit()
        tkinter.messagebox.showinfo("Message", "la modification est bien faite\n(merci de cliquer sur actualiser pour voir le changement)")
    else:
        tkinter.messagebox.showinfo("Message", "rempli toutes les cases !")

def removeFiliere(idFiliere):
    if idFiliere!="":
        cursor.execute('''DELETE FROM filiere WHERE idFiliere={};'''.format(idFiliere))
        db_loc.commit()

def Filiereslist():
    lst=[]
    cursor.execute('''SELECT * FROM filiere;''')
    rows = cursor.fetchall()
    for row in rows:
        lst.append(row)
    return lst

def getFiliere(idFiliere):
    lst=[]
    cursor.execute('''SELECT idFiliere,nomFiliere FROM filiere;''')
    rows= cursor.fetchall()
    for row in rows:
        if row[0]==idFiliere:
            lst.append(row[1])
    if lst==[]:
        return "***"
    else:
        return lst[0]
def getFilieres():
    l=[]
    cursor.execute('''SELECT nomFiliere FROM filiere;''')
    rows= cursor.fetchall()
    for row in rows:
        l.append(row[0])
    return l

def getid(nomFiliere):
    cursor.execute('''SELECT idFiliere FROM filiere WHERE nomFiliere=?;''', (nomFiliere,))
    row= cursor.fetchone()
    return int(row[0])

def ShowFiliere(window):
    i=0
    for row in Filiereslist():
        window.insert(i,str(row[0])+" - "+str(row[1]))
        i=i+1

def Insertion(window):
    newWindow =Toplevel(window)
    newWindow.attributes('-topmost',True)
    newWindow.title("Ajout d'une Filiere")
    lb1= Label(newWindow,text = "id de la filiere:")
    lb1.grid(row=0, column=0, padx=5, pady=5)
    lb2= Label(newWindow,text = "Nom de la  filiere:")
    lb2.grid(row=1, column=0, padx=5, pady=5)
    my_var= StringVar(newWindow)
    my_var.set("7")
    en1 = Spinbox(newWindow, from_= 0, to = 120,textvariable=my_var) 
    en1['state'] = 'readonly' 
    en1.grid(row=0, column=1, padx=5, pady=5)
    en2 = tkinter.Entry(newWindow)
    en2.grid(row=1, column=1, padx=5, pady=5)
    bt1= tkinter.Button(newWindow, text="Enregistrer",bg="#85929E",fg="white",activebackground="#85929E",relief="ridge")
    bt1.grid(row=2,column=0, columnspan=2, padx=15, pady=15)
    bt1.config(command=lambda: addFiliere(newWindow,en1.get(),en2.get()))

def modification(window,window1):
    if(Module.tools.selected_item(window1)!=['']):

        newWindow =Toplevel(window)
        newWindow.attributes('-topmost',True)
        newWindow.title("Modification d'une filière")
        tkinter.Label(newWindow, text="le nouveau Nom de la Filiere:").grid(row=0, column=0, padx=15, pady=15)
        en1 = tkinter.Entry(newWindow)
        bt1 = tkinter.Button(newWindow, text="Enregistrer",bg="#85929E",fg="white",activebackground="#85929E",relief="ridge")
        en1.insert(0, Module.tools.selected_item(window1)[1])
        en1.grid(row=0, column=1, padx=5, pady=5)
        bt1.grid(row=5, column=0,columnspan=2, padx=15, pady=15)

        bt1.config(command=lambda: modifyFiliere(int(Module.tools.selected_item(window1)[0]),en1.get()))
    else:
        result = tkinter.messagebox.showinfo("Message", "sélectionnez d'abord la filière que vous voulez modifier  ", icon='warning')

def suppression(window1):
    if(Module.tools.selected_item(window1)!=['']):
        result = tkinter.messagebox.askquestion("Message", "Êtes-vous sûr de vouloir supprimer la filière : "+Module.tools.selected_item(window1)[1]+" ?", icon='warning')
        if result == 'yes':
            removeFiliere(int(Module.tools.selected_item(window1)[0]))
            tkinter.messagebox.showinfo("Message", "la filière "+Module.tools.selected_item(window1)[1]+"est bien supprimée\n(merci de cliquer sur actualiser pour voir le changement)")
    else:
        result = tkinter.messagebox.showinfo("Message", "sélectionnez d'abord la filière que vous voulez supprimer ", icon='warning')
