
Projet Dijkstras

Afin d'utiliser le programme, il faut avoir installe Graphviz et matplotlib

Comment utiliser:


Creation d'un graphe:
---------------------
graph = Network()

Ajouter un lien entre A <-----> B de cout 4 et 6
------------------------------------------------
graph.ajouter_arete(A, B, 4, 6)


Utiliser une des version Dijkstras:
-----------------------------------
graph.dijkstras_naive(start, end)
graph.dijkstras_binary_heap(start, end)
graph.dijkstras_fibonnacci_heap(start, end)


Creation et Voir le graph
-------------------------

il faut tout d'abord creer la version visuel avec : graph.make_graph() 
Enstuie : graph.show() pour voir le graph.

Generer un graphe:
------------------

graph = generate_graph(size, max_connections, max_distance)

avec : size = nombre de sommets
       max_connections = le nombre max de connection qu'un sommet peut avoir
       max_distance = distance entre deux points maximale 


Tester les diffrenetes vertions
------------------------------

compare_speed(start, end, step, precision)
avec : 
    start = taille minimum du graph
    end = taille maximale du graphe
    step = marche prise a chaque etape
    precision = le nombre de foi teste pour avoir moyenne plus precise



