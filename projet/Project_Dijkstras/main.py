from fibonacci_heap import *
from binary_heap import *
import random
from graphviz import Digraph, Graph


class Network:
    """
    Class Network, pour le graphe qui represente un reseau
    """

    def __init__(self):
        self.adj = {}
        
    def ajouter_sommet(self,s):
        if s not in self.adj:
            self.adj[s] = []
            
    def ajouter_arete(self, s1, s2, dis_1, dis_2):
        self.ajouter_sommet(s1)
        self.ajouter_sommet(s2)
        if s2 not in self.adj[s1]:
            self.adj[s1].append((s2, dis_1))
            self.adj[s2].append((s1, dis_2))
        
    def arete(self,s1,s2):
        return s2 in self.adj[s1]
    
    def supprimer_arete(self, s1, s2):
        if self.arete(s1, s2):
            self.adj[s1].remove(s2)
            self.adj[s2].remove(s1)
    
    def sommets(self):
        return list(self.adj.keys())

    def voisins(self,s):
        return self.adj[s]


    def one_way_nodes(self):
        """Fonction qui donne les sommets et leurs arete mais les paires uniques       (1, 2) = (2, 1)

        Returns:
            list(tuples): les sommets et aretes
        """
        nodes = set()
        for x in self.adj:
            for y in self.adj[x]:
                pair = (max((x, y[0])), min((x, y[0])))
                if pair not in nodes:
                    nodes.add(pair)
        return nodes

    def dijkstras_naive(self, start_node, end_node):
        """
        implementaion de Dijkstras version naive

        Args:
            start_node (int): sommet de debut
            end_node (int): sommet de fin

        Returns:
            list : chemin le plus court de start_node a end_node
        """
        
        file = []
        path = {x:[None, 10**10] for x in self.sommets()}
        visited = {x:False for x in self.sommets()}
        file.append([start_node, 0])
        visited[start_node] = True
        while file:
            file.sort(key=lambda x:x[1])
            node, path_leng = file.pop(0)
            visited[node] = True



            for x in self.voisins(node):
                if not visited[x[0]]:
                    file.append((x[0], path_leng+x[1]))
                    if path_leng+x[1] < path[x[0]][1]:
                        path[x[0]] = [node, path_leng+x[1]]


        return build_path(path, start_node, end_node)


                    


    def dijkstras_binary_heap(self, start_node, end_node):
        """
        Implementation de Dijkstras avec un Binary Heap

        Args:
            start_node (int): sommet de debut
            end_node (int): sommet de fin

        Returns:
            list : chemin le plus court de start_node a end_node
        """
        file = BinHeap()
        path = {x:[None, 10**10] for x in self.sommets()}
        visited = {x:False for x in self.sommets()}
        file.insert((0, start_node))
        visited[start_node] = True
        while file.len() > 0:
            path_leng, node  = file.delMin()
            visited[node] = True


            for x in self.voisins(node):
                if not visited[x[0]]:
                    file.insert((path_leng+x[1], x[0]))
                    if path_leng+x[1] < path[x[0]][1]:
                        path[x[0]] = [node, path_leng+x[1]]


        return build_path(path, start_node, end_node)



    def dijkstras_fibonnacci_heap(self, start_node, end_node):

        """
        Implementation de Dijkstras avec un Fibonacci Heap

        Args:
            start_node (int): sommet de debut
            end_node (int): sommet de fin

        Returns:
            list : chemin le plus court de start_node a end_node
        """

        file = FibonacciHeap()
        path = {x:[None, 10**10] for x in self.sommets()}
        visited = {x:False for x in self.sommets()}
        file.insert_node(0, start_node)
        visited[start_node] = True
        while file.length() > 0:
            path_leng, node  = file.extract_min()
            visited[node] = True

            
            for x in self.voisins(node):
                if not visited[x[0]]:
                    file.insert_node(path_leng+x[1], x[0])
                    if path_leng+x[1] < path[x[0]][1]:
                        path[x[0]] = [node, path_leng+x[1]]

        return build_path(path, start_node, end_node)



    def make_graph(self):
        """Représentation graphique avec graphviz"""
        self.G = Graph('G', filename='hello')
        
        for x in self.one_way_nodes():
                self.G.edge(str(x[0]), str(x[1]))

        return self.G

    def update_graph(self, path):
        """
        Rend un chemin vert, utilise pour montrer le chemin le plus court entre deux sommets

        Args:
            path (list): chemin pris


        """
    
        for x in range(len(path)-1):
            self.G.edge(str(path[x]), str(path[x+1]), color="green")
        
        return None

    
    def show(self):
        """
        Fonction pour afficher le Graph
        """
        self.G.view()

    



def build_path(path, start, end):
    
    """
    Fonction qui reconstruit le chemin pris pour aller d'un sommet a un autre.

    Returns:
        list : le chemin pris
    """

    path_taken = []

    current = end
    while current is not None:
        path_taken.append(current)
        current = path[current][0]
    
    path_taken.reverse()
    return path_taken




def generate_graph(size, max_connections, max_distance):

    """
    Fonction qui genere un graph avec les parameteres qui lui sont donnees. 

    size = nombre de sommets
    max_connections = le nombre max de connection qu'un sommet peut avoir
    max_distance = distance entre deux points maximale

    Returns:
        Network: renvoie le graph genere
    """
    
    nodes = [x for x in range(size)]
    tree = Network()
    
    for x in nodes:
        if x not in tree.adj:
            tree.ajouter_sommet(x)
        
        potenital_nodes = random.sample(nodes, max_connections)
        for _ in range(random.randint(1, max_connections)):
            distance = random.randint(1, max_distance)
            if x == potenital_nodes[_]:
                potenital_nodes[_] = random.choice(nodes)
            
            if not (potenital_nodes[_] in tree.adj and len(tree.voisins(potenital_nodes[_])) >= max_connections):
                if (potenital_nodes[_] not in [x[0] for x in tree.voisins(x)]):
                    tree.ajouter_arete(x, potenital_nodes[_], distance, distance)
            
    
    
    #dfs pour verfier connexite du graphe, si pas connexe alors ajout des arêtes pour le rendre connex
    visited = [False for x in range(size)]
    
    q = [0]
    amnt_visited = 1

    while amnt_visited < size:

        node = q.pop(-1)
        
        for x in tree.voisins(node):
            if not visited[x[0]]:
                q.append(x[0])
                visited[x[0]] = True
                amnt_visited += 1
        
        if q == []:
            new_link_node = visited.index(False)
            tree.ajouter_arete(node, new_link_node, 5, 5)
            q.append(new_link_node)
            visited[new_link_node] = True
            amnt_visited += 1

    return tree
        


    





    

import time
import matplotlib.pyplot as plt

def compare_speed(start, end, step, precision):

    """
    Fonction utiliser pour mesure et compare les differents algos

    start = taille minimum du graph
    end = taille maximale du graphe
    step = marche prise a chaque etape
    precision = le nombre de foi teste pour avoir moyenne plus precise

    * = lignes a suprime si testes plus difficiles

    """

    fibo_times = []
    binary_times = []
    naive_times = []
    x_axis = []

    for x in range(start, end, step):
        print(x)
        fibo_time, heap_time, naive_time = 0, 0, 0
        x_axis.append(x)
        graph = generate_graph(x, 4, 10)
        for y in range(precision):

            
            
            start_node = random.randint(0, len(graph.sommets())-1)
            end_node = random.randint(0, len(graph.sommets())-1)


            start = time.time()
            path = graph.dijkstras_fibonnacci_heap(start_node, end_node )
            fibo_time +=  time.time() - start
        
            

            start = time.time()
            path = graph.dijkstras_binary_heap(start_node, end_node )
            heap_time += time.time() - start

            start = time.time() #*
            graph.dijkstras_naive(1, len(graph.sommets())-1) #*
            naive_time += time.time() - start #*

        fibo_times.append(fibo_time/precision)
        binary_times.append(heap_time/precision)
        naive_times.append(naive_time/precision) #*


        
    
    print("Fibo Time :", fibo_time, "Heap Time :", heap_time, "Naive Time:", naive_time)
    plt.plot(x_axis, fibo_times)
    plt.plot(x_axis, binary_times)
    plt.plot(x_axis, naive_times) #*

    plt.xlabel('Nombre de Sommets')
    plt.ylabel('Temps (sec)')
    
    plt.title('Comparaison Fibo, Heap and force brute')
    
    plt.show()



        #exemples
#---------------------------------
#graph = generate_graph(100, 2, 10)
#path = graph.dijkstras_fibonnacci_heap(1, 32)

    #voir le graph avec le chemin
#graph.make_graph()
#graph.update_graph(path)
#graph.show()

    #comparaison des vitesse
#compare_speed(400, 1000, 50, 5)







