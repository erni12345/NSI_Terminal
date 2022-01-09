def supprime_doublons(lst):

    vu = {} # Rechercher dans un dico ==> O(1)
    
    finalList = []

    for x in lst:
        if x not in vu:
            finalList.append(x)
            vu[x] = True

    return finalList




