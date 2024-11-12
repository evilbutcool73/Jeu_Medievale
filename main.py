from src.controllers import *
from src.models import *
from src.views import *

game = GameController()

roturier1 = Roturier("Roturier 1", 20, 10, 10, 10, 5)
roturier2 = Roturier("Roturier 2", 20, 10, 10, 10, 5)
paysan1 = Paysan("Paysan 1", 20, 20, 15, 5)

joueur = Noble("joueur", 20, 0, 0, 5)

# Création du village
village_joueur = Village("Village du Joueur")

# Ajout d'habitants
for i in range(5):
    village_joueur.ajouter_habitant(Roturier(f"Roturier {i+1}", age=20 + i))
for i in range(3):
    village_joueur.ajouter_habitant(Paysan(f"Paysan {i+1}", age=25 + i))

# Calcul de la production et perception des impôts
village_joueur.produire_ressources()
village_joueur.percevoir_impots()

# Afficher le statut du village
village_joueur.afficher_statut()


