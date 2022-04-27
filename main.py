from tkinter import *

import Module.Etudiant
import Module.filiere
import Module.tools 

import tkinter.messagebox



root = Tk()
root.title("Mini-Projet")

#################### partie 1 #######################
frame_Etudiant = LabelFrame(root, text="Etdiant",pady=10,borderwidth=0)
frame_Filiere = LabelFrame(root, text="Filiere",pady=10,borderwidth=0)
frame_outils=LabelFrame(root, text="outils", pady=2)

scrool1=Scrollbar(frame_Etudiant,orient='vertical')
scrool2=Scrollbar(frame_Filiere,orient='vertical')

scrool3=Scrollbar(frame_Etudiant,orient='horizontal')
scrool4=Scrollbar(frame_Filiere,orient='horizontal')


List_Etudiant = Listbox(frame_Etudiant ,activestyle='none',selectforeground='Black',width=60,yscrollcommand = scrool1.set, borderwidth=0, highlightthickness=0)
List_Filiere= Listbox(frame_Filiere ,activestyle='none',selectforeground='Black',width=60, yscrollcommand = scrool2.set, borderwidth=0, highlightthickness=0)

scrool1['command'] =List_Etudiant.yview
scrool2['command'] =List_Filiere.yview

scrool3['command'] =List_Etudiant.xview
scrool4['command'] =List_Filiere.xview

bouton_ajouter_E = Button(frame_outils, text='ajouter un etudiant',relief="ridge")
bouton_supprimer_E = Button(frame_outils, text='supprimer un etudiant',bg="#D62F2F",fg="white", activebackground="#D62F2F",relief="ridge")
bouton_modifier_E = Button(frame_outils, text='modifier un etudiant',relief="ridge")

bouton_actualiser = Button(frame_outils, text='actualiser',bg="#2B9486",fg="white",activebackground="#2B9486",relief="ridge")

bouton_ajouter_F = Button(frame_outils, text='ajouter une Filiere',relief="ridge")
bouton_supprimer_F = Button(frame_outils, text='supprimer une Filiere',bg="#D62F2F",fg="white",activebackground="#D62F2F",relief="ridge")
bouton_modifier_F = Button(frame_outils, text='modifier une Filiere',relief="ridge")


frame_Etudiant .grid(column=0,row=0,padx=10,pady=5)
frame_Filiere.grid(column=1,row=0,padx=10,pady=5)

frame_outils.grid(column=0,columnspan=2,row=1,padx=10,pady=10)
List_Etudiant.grid()
scrool1.grid(column=1,row=0,sticky='ns')
List_Filiere.grid()
scrool2.grid(column=1,row=0,sticky='ns')

scrool3.grid(column=0,row=1,columnspan=2)
scrool4.grid(column=0,row=1,columnspan=2)

bouton_ajouter_E.grid(row=0,column=0,sticky="we",padx=10,pady=5)
bouton_modifier_E.grid(row=0,column=1,sticky="we",padx=10,pady=5)
bouton_supprimer_E.grid(row=1,column=0,columnspan=2,sticky="we",padx=10,pady=5)

bouton_actualiser.grid(row=0,column=3,sticky="we",padx=10,pady=5)

bouton_ajouter_F.grid(row=0,column=4,sticky="we",padx=10,pady=5)
bouton_modifier_F.grid(row=0,column=5,sticky="we",padx=10,pady=5)
bouton_supprimer_F.grid(row=1,column=4,columnspan=2,sticky="we",padx=10,pady=5)


#################### partie 2 #######################
Module.Etudiant.ShowStudents(List_Etudiant)
Module.filiere.ShowFiliere(List_Filiere)
#################### partie 3 Etudiant #######################
bouton_ajouter_E.config(command=lambda:Module.Etudiant.Insertion(root))
bouton_supprimer_E.config(command=lambda:Module.Etudiant.suppression(List_Etudiant))
bouton_modifier_E.config(command=lambda:Module.Etudiant.modification(root,List_Etudiant))
#################### partie 3 filières #######################
bouton_ajouter_F.config(command=lambda:Module.filiere.Insertion(root))
bouton_supprimer_F.config(command=lambda:Module.filiere.suppression(List_Filiere))
bouton_modifier_F.config(command=lambda:Module.filiere.modification(root,List_Filiere))
####################partie 3 filières#######################

def actualiser(window1,window2):
    Module.tools .destroy(window2)
    Module.tools .destroy(window1)
    Module.Etudiant.ShowStudents(window1)
    Module.filiere.ShowFiliere(window2)

bouton_actualiser.config(command=lambda:actualiser(List_Etudiant,List_Filiere))

###########################################################

root.mainloop()