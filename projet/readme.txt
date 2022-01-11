Utilisation


RLE.py
#-----decompression------
run_decompress("franck_comp") #nom du fichier sans l’extension pgm
#-----compression------
run_compress("franck") #nom du fichier sans l’extension pgm 






huffman_texte.py


compress("projet/tristram_shandy.txt")
compress("projet/adn.txt") # --> compression + création du ficher adn_compressed.txt
decompression_avec_dico("projet/adn_compressed.txt")# --> decompression + creation du ficher
# si on sauvgarde l'arbre decompression_avec_arbre("projet/adn_compressed.txt", arbre) --> decompression + creation du ficher


huffman_image.py




compress("projet/Logo_Python.pgm") # --> compression + création du ficher adn_compressed.txt
decompression_avec_dico("projet/Logo_Python_compressed.pgm")# --> decompression + creation du fichier
# si on sauvgarde l'arbre decompression_avec_arbre("projet/Logo_Python_compressed.pgm", arbre) --> decompression + creation du ficher