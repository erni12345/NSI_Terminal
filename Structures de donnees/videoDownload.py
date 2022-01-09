"""import datetime
from pytube import YouTube



yt = YouTube('https://www.youtube.com/watch?v=cFWeW1pBYkM&ab_channel=SumerianRecords').streams.filter(progressive=True)
print(yt)

class Film:
    def __init__(self, titre, realisateur):
      self.titre = titre
      self.realisateur = realisateur
 
class Personne:
    def __init__(self, nom, annee_naissance, annee_mort, lieu_naissance):
      self.nom = nom
      self.annee_naissance = annee_naissance
      self.annee_mort = annee_mort
      self.lieu_naissance = lieu_naissance


    def age(self):

        if self.annee_mort < datetime.date.today().year:
            return None

        else:

            age = datetime.date.today().year - self.annee_naissance
            return age




lautner = Personne("Georges Lautner", 1926, 2013, "Nice")

print(f"{lautner.nom} est une personne née à {lautner.lieu_naissance} en {lautner.annee_naissance}")

tonton = Film("Les tontons flingueurs", lautner)

print(f"{tonton.titre} est un film réalisé par {tonton.realisateur.nom} originaire de {tonton.realisateur.lieu_naissance}")





def test():
    print("worked")


a = {"try" : test()}

a["try"]"""



