from PIL import Image

image = Image.open("joconde.jpg")
largeur, hauteur = image.size

image.getpixel((10, 10))

im_copy = Image.new("RGB",(largeur, hauteur))




def rota90(image):
    """

    Complexite == O(n^2)
    """
    for y in range(hauteur):
        for x in range(largeur):
            rgb = image.getpixel((x, y))
            im_copy.putpixel((y, largeur - 1 - x), rgb)

    im_copy.show()



def echange_pixel(image, x0, y0, x1, y1):

    rgb = image.getpixel((x0,y0))
    rgb2 = image.getpixel((x1,y1))
    image.putpixel((x1, y1), rgb)
    image.putpixel((x0, y0), rgb2)



def echange(img, x0, y0, x1, y1, n):
    
    for x in range(0, n):
        for y in range(0, n):
            echange_pixel(image, x0+x, y0+y, x1+x, y1+y)



def permutaion_circ(image, x0, y0, n):

    echange(image, x0, y0, x0 + (n)//2, y0, n)
    echange(image, x0, y0, x0 + (n)//2, y0+(n)//2, n)
    echange(image, x0, y0, x0, y0+(n)//2, n)




def tourne_quadrants(image, x0, y0, n):

    if n >= 2:
        n = n//2
        tourne_quadrants(image, x0, y0, n)
        tourne_quadrants(image, x0, y0 + n, n)
        tourne_quadrants(image, x0+n, y0, n)
        tourne_quadrants(image, x0 + n, y0 + n, n)
        echange(image, x0, y0, x0 + n, y0, n)
        echange(image, x0, y0, x0 + (n), y0+(n), n)
        echange(image, x0, y0, x0, y0+(n), n)




tourne_quadrants(image, 0, 0, largeur)
image.show()
    
