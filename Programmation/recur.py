def logistique(p, n):
    if n == 0:
        return 0.5

    else:
        return p*logistique(p,n-1)*(1-logistique(p,n-1))



print(logistique(3,3))