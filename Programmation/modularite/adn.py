"""
ADN MODULE





"""
import random


BASE_COMPLEMENTAIRE = {"A":"T", "T":"A", "G":"C", "C":"G"}
def lit_sequence(path):
    """
    prend en argument un nom de fichier sous forme d'une
    chaîne de caractères et renvoie la séquence d'ADN lue dans le fichier sous forme
    d'une chaîne de caractères

    """
    with open(path) as f:
        lines = f.readline()
        return lines


def sequence_aleatoire(taille):

    """
    prend en argument un entier et renvoie une
    séquence aléatoire d'ADN de la taille de l’entier donné sous forme d'une chaîne de
    caractères.
    """
    sequence = ""

    for x in range(taille):
        sequence += ["C", "T", "G", "A"][random.randint(0,3)]
    return sequence


def sequence_complementaire(sequence_base):

    """
    prend en argument une séquence d'ADN
    sous forme d'une chaîne de caractères et renvoie la séquence complémentaire
    inverse en chaine de caractères
    """
    sequence = ""
    
    for x in sequence_base:
        sequence.append(BASE_COMPLEMENTAIRE[x])

    return sequence[::-1]


def proportion_gc(sequence_base):

    """prend en argument une séquence d'ADN sous forme
    d'une chaîne de caractères et renvoie la proportion en GC de la séquence sous
    forme d'un float.

    """
    n_gc = 0
    for x in sequence_base:
        if x in ["G", "C"]:
            n_gc += 1

    return n_gc/len(sequence_base)