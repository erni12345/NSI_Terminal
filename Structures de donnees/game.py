import csv
import random


class Joueurs:

    def __init__(self, nom, pseudo,victoires,niveau):

        self.nom = nom  
        self.pseudo = pseudo  
        self.victoires = victoires  
        self.niveau = niveau
        self.points = 0
        self.coups = 0
    

    def nouvelle_victoire(self):

        self.victoires += 1

    def actualisation_niveau(self):

        self.niveau = (self.victoires // 10) + 1

    
    def nouvelle_partie(self):

        self.points = 0
        self.coups = 0




def creer_dico_instances(nom_csv, Joueur):

    f = open(nom_csv, 'r')
    reader = csv.DictReader(f, delimiter = ";")

    noms = []

    for x in reader:
        noms.append(dict(x))

    dico_joueurs = {x['nom'] : Joueur(x['nom'], x['pseudo'], x['victoires'], x['niveau']) for x in noms}

    return dico_joueurs



a = creer_dico_instances('joueurs.csv', Joueurs)

print(a["Anne"].pseudo)



def apparier_joueurs(dic, n):

    players = list(dic.keys())
    random.shuffle(players)
    fighting_players = []

    for x in range(0, n*2, 2):
        fighting_players.append([{players[x]:dic[players[x]]}, {players[x+1]:dic[players[x+1]]}])

    return fighting_players

a['Anne'].victoires

help(random.randint)

print(apparier_joueurs(a, 4))

