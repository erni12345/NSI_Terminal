import doctest


def recherche_dicho(start, end, lst,v):
    """Recherche Dichotomique

    Args:
        lst ([type]): liste trie de nombres
        v ([type]): la valeur recherche

    Returns:
        [type]: indice de l'element, -1 
    """
    
    if end >= 1:
        mid = 1 + (end - start) //2    
        if lst[mid] == v:
            return mid
        elif lst[mid] > v:
            return recherche_dicho(start, mid-1, lst, v)
        else:
            return recherche_dicho(start, mid+1, lst, v)
    else:
        return -1



lst = [1,2,3,4,5,6,7,8]
print(recherche_dicho(0,8,lst,6))