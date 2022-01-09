import sys
import os

def read_pgm_file(file):
    """
    Fonction qui renvoie une image PGM en matrice representant l'image

    Args:
        file (ficher PGM): image pgm a ouvrire

    Returns:
        Renvoie les informations de l'image ainsi que la matrice de l'image
    """

    header = file.readline()
    width, height = [int(i) for i in file.readline().split()]
    scale = int(file.readline())
    image = []

    for x in range(height):
        line = []
        for y in range(width):
            line.append(int(file.readline()))
        image.append(line)


    return image, width, height, scale, header

def compression(image, width, height):
    """
    Fonction qui comporesse image PGM

    Args:
        image (matrice): Image a compresser
        width (int): largeur image
        height (int): hauteur image

    Returns:
        renvoie l'image compresse
    """
    new = []

    for x in range(height):
        mid = []
        amount = 1
        for y in range(width):
            if y == width-1:
                mid.append(amount)
                mid.append(image[x][y])

            elif image[x][y] == image[x][y+1]:
                amount += 1
            else:
                mid.append(amount)
                mid.append(image[x][y])
                amount = 1
        new.append(mid)
    
    return new


def compare_size(file_name):

    """
    Summary : Fonction qui calcule le taux de compression

    IN :
        og_image[list] : imaeg original
        compressed_image[list] : image apres compression

    
    """


    og_image_size = float(os.stat(f"projet/{file_name}.pgm").st_size)
    compressed_image_size = float(os.stat(f"projet/{file_name}_comp.pgm").st_size)

    
    improvement = (1 - (compressed_image_size/og_image_size))*100
    print(f"Taille de l'image originale : {og_image_size} (bytes)")
    print(f"Taille de l'image compresse : {compressed_image_size} (bytes)")
    print(f"Taux de compression : %{improvement} (si negatif alors l'image est devenue plus grande)")


        

def run_compress(file_name):
    """
    Fonction qui fait la compression en general, et sauvgarde le nouveau ficher

    Args:
        file_name (string): le nom du ficher
    """
    image = []
    width = 0
    height = 0
    scale = 0

    with open(f"projet/{file_name}.pgm", "r") as ft:
        image, width, height, scale, header = read_pgm_file(ft)

    compressed_image = compression(image,width, height)

    with open(f"projet/{file_name}_comp.pgm", "w") as ft:
        ft.write(header)
        ft.write(f"{width} {height}" + "\n")
        ft.write(str(scale) + "\n")
       
        for x in compressed_image:
            for y in x:
                ft.write(str(y) + '\n')


    compare_size(file_name)
        




def read_pgm_file_decompress(file):
    """Fonction qui lit et renvoie la liste representant l'image a decompresser

    Args:
        file (OBJECT): le ficher a decompresser

    Returns:
        Differents elements et caracteristique duu ficher (width, height, scale, header)
    """

    header = file.readline()
    width, height = [int(i) for i in file.readline().split()]
    scale = int(file.readline())
    image = []

    for x in range(height * width):
        var = file.readline()
        var.strip()
        if var != "":
            image.append(int(var))


    return image, width, height, scale, header


def decompress(image, width, height):
    """focntion qui decompresse l'image
        On parcours que les indice paire, et puis on ajoute le nombre de fois sur l'indice l'element suivant
        l = [3, 5, 6, 7]
        [3, 5, 6, 7] --> [ l[0] * l[0+1], l[2] * l[2+1] ]--> [3*5, 6*7] --> [5, 5, 5, 7, 7, 7, 7, 7, 7]


    Args:
        image (list): l'image a decompresser
        width (int): largeur
        height (int): hauteur

    Returns:
        image decompresse
    """
    image_deco = []

    for x in range(0, len(image),2):
        for y in range(image[x]):
            image_deco.append(image[x+1])
    
    return image_deco



def run_decompress(file_name):
    """
    Fonction qui s'occupe de toute la decompression de l'image

    Args:
        file_name (str  ): nom du ficher
    """
    with open(f"projet/{file_name}.pgm", "r") as ft:
        image, width, height, scale, header = read_pgm_file_decompress(ft)
        decompressed_image = decompress(image, width, height)

    with open(f"projet/{file_name}_deco.pgm", "w") as ft:
        ft.write(header)
        ft.write(f"{width} {height}" + "\n")
        ft.write(str(scale) + "\n")
        for x in decompressed_image:
            ft.write(str(x) + '\n')


run_compress("Logo_Python")

