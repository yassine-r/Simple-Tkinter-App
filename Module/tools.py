import Module.Etudiant
import Module.filiere
def destroy(window):
    window.delete(0,'end')

def selected_item(window):
    x=""
    for i in window.curselection():
        x=x+str(window.get(i))
    lst=x.split(" - ")
    return lst
