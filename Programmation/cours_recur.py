

def fibonacci(n):
    """
    n = entier --> entier
    renvoie le chiffre au n'eme terme de la suite fibonacci
    avec recusivite


    """
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n-1)+fibonacci(n-2)





def puissance_iter(a, n):
    if n == 0:
        return 1

    else:
        start = 1
        for x in range(n):
            start *= a

        return start



def puissance_recur(a, n):

    if n == 0:
        return 1

    else:
        return a * puissance_recur(a, n-1)

"""import turtle as t

def koch(longueur, n):
    if n == 0:
        t.forward(longueur)
    else:
        koch(longueur/4, n-1)
        t.left(60)
        koch(longueur/3, n-1)
        t.right(120)
        koch(longueur/3, n-1)
        t.left(60)
        koch(longueur/3, n-1)

def flocon(taille, etape):
    koch(taille, etape)
    t.right(120)
    koch(taille, etape)
    t.right(120)
    koch(taille, etape)

flocon(200, 10)
"""

import turtle as t

"""t.bgcolor("cyan")
t.speed(0)
t.setx(-100)
t.sety(-100)"""
def courbe_koch(leng, n):

    if n == 0:
        t.forward(leng)
    else:
        courbe_koch(leng/3, n-1)
        t.left(90)
        courbe_koch(leng/3, n-1)
        t.right(90)
        courbe_koch(leng/3, n-1)
        t.right(90)
        courbe_koch(leng/3, n-1)
        t.left(90)
        courbe_koch(leng/3, n-1)
        


#courbe_koch(1000, 5)

import sys

sys.setrecursionlimit(10000)

def lst_n(n):
    
    if n == 0:
        return [0]
    return [n] + lst_n(n-1)


def syracuse(u):
    """
    int -> list
    renvoie les termes de la suite de Syracuse de premier terme 
    donné en paramètre
    """
    if u == 1:
        return[1]
    
    else:
        if u % 2 == 0:
            u = u//2
        else:
            u = (3*u) + 1

        return [u] + syracuse(u)


"""import numpy as np
import matplotlib.pyplot as plt   
def syracuse_len(u):
    
    int -> int
    renvoie la longueur de la suite de Syracuse
    de premier terme donné en paramètre
    
    return len(syracuse(u))

l = []
t = np.arange(1,10000)
for i in t:
    l = l + [syracuse_len(i)]   

plt.plot(np.log(t), np.log(l))
#plt.plot(t, l)"""
print(syracuse(13))


