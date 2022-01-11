import os

#--------Class Node Pour Arbre --------
class Node:
    def __init__(self, prob, symbol, left=None, right = None):
        self.prob = prob
        self.symbol = symbol
        self.left = left
        self.right = right
        self.code = ""




#---------- CODE COMPARAISON TAILLE FICHER ------------------

def compare_size(data, encoded):
    
    """
    Summary : Fonction qui calcule le taux de compression
    On ne peut pas utiliser la taille du ficher car python ne stock pas les 0 et 1 comme des bits mais des valeurs sur 8 bits

    IN :
        data[string] : string original
        encoded[string] : string apres compression

    
    """
    avant_compression = len(data)*8
    apres = len(encoded)
    

    improvement = (1-apres/avant_compression)*100
    print(f"Taille du ficher originale : {avant_compression} (bytes)")
    print(f"Taille du ficher apres compression : {apres} (bytes)")
    print(f"Taux de compression : %{improvement} (si negatif alors l'image est devenue plus grande)")


#---------Compression ---------------

def dico_de_proba(file):
    """Creation du dico de nombre d'occurence

    Args:
        file (string): string dans le ficher.txt

    Returns:
        dic: dictionnaire du nombre d'occurences
    """
    dico = dict()
    for e in file:
        if e in dico:
            dico[e] += 1
        else:
            dico[e] = 1
    return dico


codes = {}

def calculer_symbole(node, val=""):
    """Codification des valeurs dans le dico d'occurence

    Args:
        node (class node): Arbre de Huffman
        val (string, optional): valeur utiliser dans recurrence pour creer le code de chaque valuer. Defaults to "".

    Returns:
        dico: dico d'encodage
    """
    n_val = val + str(node.code)
    if node.left:
        calculer_symbole(node.left, n_val)
    if node.right:
        calculer_symbole(node.right, n_val)
    
    if not node.left  and not node.right:
        codes[node.symbol] = n_val
    
    return codes


def encodage(data, dico_codage):
    """Encodage du text

    Args:
        data (string): string representant le ficher    
        dico_codage (dict): dico des valuers en code

    Returns:
        string  : encodage 
    """

    out = []
    for c in data:
        out.append(dico_codage[c])
    
    string = "".join([str(i) for i in out])
    return string


def compression_Huffman(file):
    """Fonction d'encodage huffman --> Creation des dico + arbre + encodage

    Args:
        file (string): representation string du ficher

    Returns:
        str, class Node, dict: encodage, Arbre huffman, dico_encodage
    """
    dico_proba = dico_de_proba(file)
    caract = dico_proba.keys()
    probas = dico_proba.values()

    nodes = []

    for c in caract:
        nodes.append(Node(dico_proba.get(c), c))

    while len(nodes)>1:
        nodes = sorted(nodes, key=lambda x:x.prob)
        right = nodes[0]
        left = nodes[1]

        left.code = 0
        right.code = 1
        
        newNode = Node(left.prob+right.prob, left.symbol+right.symbol, left, right)

        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newNode)

    dico_encodage = calculer_symbole(nodes[0])
    encodage_ = encodage(file, dico_encodage)
    return encodage_, nodes[0], dico_encodage




def open_file(file):
    """ouvre ficher et return le string representant le ficher
    """
    with open(file, 'r', encoding="utf-8") as file:
        data = file.read().replace('\n', '')
    
    return data

def wrtie_file(dico, compressed_file, file):
    """Ecrit et cree un nouveau ficher (version apres compression)

    Args:
        dico (dict): dico de compression
        compressed_file (string): string qui represent la compression
        file (string): nom du ficher
    """

    with open(file+"_compressed.txt", 'w', encoding="utf-8") as file:
        file.write(str(dico))
        file.write("\n")
        file.write(str(compressed_file))

def compress(file):
    """Fonction qui s'occupe de toute la compression + sauvgarde nouveau ficher 

    Args:
        file (string): nom du ficher

    Returns:
        class Node: arbre huffman de la compression
    """
    text = open_file(file)
    compressed = compression_Huffman(text)

    ficher_comprime, arbre_huffman ,dico_compression  = compressed


    wrtie_file(dico_compression, ficher_comprime, file[:-4])

    compare_size(text, ficher_comprime)
    return arbre_huffman






#------------------- Decompression --------------

def write_deco(ficher, string):
    """Creation nouveau ficher apres decompression

    """
    with open(ficher+"_decompression.txt", "w", encoding = "utf-8") as ft:
        ft.write(string)





#---------------- Decompression avec ficher mais sans arbre, le ficher doit avoir le dico en entete ----------------------

def huffman_decompression_avec_dico(ficher, dico):
    """Decompression Huffman avec dictionnaire et non avec arbre

    Args:
        ficher (string): representation binaire du ficher
        dico (dict): dico pour decodage

    Returns:
        string: ficher apres decompression
    """
    
    start = 0
    end = 1
    check = {dico[x]:x for x in dico}
    string = ""
    for x in range(len(ficher)):

        current = ficher[start:end]
        if current in check:
            string += check[current]
            start = end
        end += 1

    return string



        
import ast

def decompression_avec_dico(ficher):
    """Ficher qui s'occupe de la decompression

    Args:
        ficher (string): nom du ficher
    """

    with open(ficher, "r", encoding="utf-8") as ft:
        dico = ast.literal_eval(ft.readline())
        data = ft.readline().replace('\n', '')
    
    string = huffman_decompression_avec_dico(data, dico)
    write_deco(ficher[:-4], string)





#------Decompression avec arbre (class Node) ----------------

def huffman_decompression_avec_arbre(ficher_encode, arbre_huffman):
    """Decompression Huffman avec arbre et non avec dictionnaire

    Args:
        ficher (string): representation binaire du ficher
        arbre_huffman (class Node): arbre de Huffman

    Returns:
        string: ficher apres decompression
    """
    head = arbre_huffman
    decompression = []
    for x in ficher_encode:
        if x == '1':
            arbre_huffman = arbre_huffman.right   
        elif x == '0':
            arbre_huffman = arbre_huffman.left
        try:
            if arbre_huffman.left.symbol == None and arbre_huffman.right.symbol == None:
                pass
        except AttributeError:
            decompression.append(arbre_huffman.symbol)
            arbre_huffman = head
        
    string = ''.join([str(item) for item in decompression])
    return string


def decompression_avec_arbre(ficher, arbre):
    """Ficher qui s'occupe de la decompression

    Args:
        ficher (string): nom du ficher
    """
    string = open_file(ficher)

    decompression = huffman_decompression_avec_arbre(string, arbre)

    write_deco(ficher[:-4], decompression)



#compress("projet/tristram_shandy.txt")
#compress("projet/adn.txt") --> compression + creatin du ficher adn_compressed.txt
#decompression_avec_dico("projet/adn_compressed.txt") --> decompression + creation du ficher
# si on sauvgarde l'arbre decompression_avec_arbre("projet/Logo_Python_compressed.pgm", arbre) --> decompression + creation du ficher 