import doctest

def factoriel(n):
  assert type(n) == int, "n doit etre un entier"
  assert n >= 0, "n doit etre superieur ou egal a 0"

  if n == 0:
    return 1
  else:
    chiffre = 1
    for x in range(1, n+1):
      chiffre *= x
    return chiffre






def test_factoriel():

  test = [1,2,3,4,5,6]
  reponse = [1,2,6,24,120,720]

  for x in test:
    check = factoriel(x)
    assert check == reponse[x-1], f" ne marche pas, got : {check}, expected : {reponse[x-1]}"

  return True


def indice_min(lst, i, n):

  """
  list, entier, entier --> entier
  renvoie l'indice du plus petit nombre de la liste

  >>> indice_min([1,2,3,4,5],1,5)
  1
  >>> indice_min([3,2,4,3,1],3,5)
  4
  
  """
  index = i
  numb = lst[index]
  for y in range(i, n):
    if numb > lst[y]:
      index = y
      numb = lst[y]

  return index


def trie_select(lst):
  """
  list de nombre --> list de nombre triee
  renvoie la liste trie du plus petit au plus grand
  >>> trie_select([3,2,1])
  [1, 2, 3]

  >>> trie_select([3,6,8,4,1])
  [1, 3, 4, 6, 8]

  >>> trie_select([1,2,3,4])
  [1, 2, 3, 4]

  >>> trie_select([1,1,1,1])
  [1, 1, 1, 1]

  >>> trie_select([1,1,2,10,432,-43,3])
  [-43, 1, 1, 2, 3, 10, 432]

  """

  for y in range(0, len(lst)-1):
    ind = indice_min(lst, y, len(lst))
    lst[ind], lst[y] = lst[y], lst[ind]

  return lst





