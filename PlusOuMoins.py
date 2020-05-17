#importations 
from tkinter import *
from random import *

#variables
nombre = randint(0,100)


#fonction logique
def valide(n):
    """Cette fonction prend en paramètre le nombre donné par l'utilisateur et le compare avec le nombre aléatoirement compris entre 0 et 100.
       Si le nombre de l'utilisateur est égal à celui aléatoire, alors la fonction renvoie 0 
       Si le nombre de l'utilisateur est supérieur à celui aléatoire, alors la fonction renvoie 1 
       Si le nombre de l'utilisateur est inférieur à celui aléatoire, alors la fonction renvoie -1 """
    if n == nombre:
        return 0
    elif n > nombre :
        return 1
    elif n < nombre:
        return -1

# Creation de la fenêtre
fenetre = Tk()
fenetre.iconbitmap("PlusOuMoins\icon.ico")
fenetre.title("Jeu du Plus ou Moins")
fenetre.geometry("275x75")

#creation des widgets
button = Button(fenetre, text = "Essayer")
champ = Entry(fenetre)
label = Label(fenetre, text = "Devine le nombre")

#Initialistion des widgets
label.pack()
champ.pack()
button.pack()

#Gestionnaire d'événement
def action_clic(e):
    """Cette fonction s'occupe de l'affichage du texte et de changer le nombre une fois gagné."""
    global nombre
    if valide(int(champ.get())) == 0:
        label.config(text = "Gagné, tu peux rejouer !")
        nombre = randint(0,100)
    elif valide(int(champ.get())) == 1:
        label.config(text ="Plus petit")
    elif valide(int(champ.get())) == -1:
        label.config(text ="Plus grand")
button.bind("<Button-1>",action_clic)

#Initialisation de la fenêtre
fenetre.mainloop()