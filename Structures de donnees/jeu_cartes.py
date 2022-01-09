# -*- coding: utf-8 -*-

from Tkinter import *   # python 2.7
#from tkinter import *   # python 3.x


# jeu 52 cartes
ListeCarte = ['c1','c2','c3','c4','c5','c6','c7','c8','c9','c10','cj','cq','ck','h1','h2','h3','h4','h5','h6','h7','h8','h9','h10','hj','hq','hk','d1','d2','d3','d4','d5','d6','d7','d8','d9','d10','dj','dq','dk','s1','s2','s3','s4','s5','s6','s7','s8','s9','s10','sj','sq','sk']

# on mélange les cartes
import random

#


def NouveauTirage():
    
    #
    
    # les images sont dans le sous-répertoire 'cards_gif'
    # index est un entier compris entre 0 et 51
    NomFichier = 'cards_gif/' + ListeCarte[index] + '.gif'    
    
    MaPhoto = PhotoImage(file = NomFichier)
    gifdict[NomFichier]= MaPhoto   # référence
    
    # affichage de l'image dans MonCanevas
      
    #
    
    
    
    
# Utilisation d'un dictionnaire pour conserver une référence
gifdict={}

Mafenetre = Tk()

# création d'un widget 'Canvas'

LARGEUR = 480 # en pixels
HAUTEUR = 360

MonCanevas = Canvas(Mafenetre, width = LARGEUR, height = HAUTEUR, bg = 'white')
MonCanevas.pack(side = TOP, padx = 10, pady = 10)

# création d'un widget 'Button'

#

# création d'un widget 'Button'

#

Mafenetre.mainloop()