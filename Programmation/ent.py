from typing import final
from math import sqrt


def carre(ls):
    return [x**2 for x in ls]


def permute(lst,i1, i2):

    a = lst.copy()

    a[i1], a[i2] = a[i2], a[i1]


    z = []

    for x in range(len(lst)):

        if x not in [i1, i2]:
            z.append(lst[x])

        elif x == i1:
            z.append(lst[i2])

        else:

            z.append(lst[i1])

    return z


def elements_positifs(lst):

    return [x for x in lst if x >= 0]



def filtre(lst,lettre):

    return [x for x in lst if x[0] == lettre]



def plus_long_mot(lst):

    lenn = len(lst[0])
    mot = lst[0]


    for x in lst:
        if len(x) > lenn:
            lenn = len(x)
            mot = x

    return mot



def indices(lst, el):
    
    return [x for x in range(len(lst)) if lst[x] == el]




def elements_communs(lst1, lst2):

    return [x for x in lst1 if x in lst2]



def supprime_doublons(lst):

    vu = {}
    
    finalList = []

    for x in lst:
        if x not in vu:
            finalList.append(x)
            vu[x] = True

    return finalList



def min2(lst):

    sortedLst = sorted(lst)

    return sortedLst[1]




def diametre(lst):

    maxLen = sqrt((lst[-1][0] - lst[0][0])**2 + (lst[-1][1] - lst[0][1])**2)

    for x in range(len(lst)):

        for y in range(x, len(lst)):

            currentLen = sqrt((lst[x][0] - lst[y][0])**2 + (lst[x][1] - lst[y][1])**2)

            if currentLen > maxLen:
                maxLen = currentLen

    return maxLen




def somme_diviseurs(n):

    divisors = []
    for x in range(1,n+1):
        if n % x == 0:
            divisors.append(x)


    return sum(divisors)



def temp_de_vol_recursive(n, e = 0):

    if n == 1:
        return e
    
    if n % 2 == 0:
        return temp_de_vol_recursive(n/2, e+1)

    else:
        return temp_de_vol_recursive((3*n) + 1, e+1)



def plus_long():
    c = []
    for x in range(1):
        a = temp_de_vol_recursive(x)
        c.append((a, x))



def fibonacci(n):
  """
  int --> int
  renvoie le n terme de la suite fibonacci
  """
  if n <= 1:
    return n
  else:
    return fibonacci(n-2)+fibonacci(n-1)




def triangle_pascal(n):

    triangle = [[1] for x in range(n)]
    
    for x in range(1,n):
        for y in range(1,x+1):
            if y == x:
                triangle[x].append(1)
            else:
                triangle[x].append(triangle[x-1][y] + triangle[x-1][y-1])

    return triangle


a = triangle_pascal(1)


def decoupe(string, c_special):
    return string.split(c_special)


print(decoupe("a b c d", " "))








    
    




    

