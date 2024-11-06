import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.models import Personne, Roturier, Paysan, Noble, Seigneur

# Création de quelques roturiers
roturier1 = Roturier("Roturier 1", age=20, ressources=50, argent=0, capacite_production=10)
roturier2 = Roturier("Roturier 2", age=25, ressources=60, argent=0, capacite_production=15)

# Création d'un noble et ajout de roturiers
noble1 = Noble("Noble 1", age=40, ressources=100, argent=50)
noble1.ajouter_roturier(roturier1)
noble1.ajouter_roturier(roturier2)

# Création d'un seigneur et ajout du noble comme vassal
seigneur = Seigneur("Seigneur", age=50, ressources=300, argent=150)
seigneur.ajouter_vassal(noble1)

# Perception des impôts
noble1.percevoir_impot()  # Le noble perçoit des impôts sur ses roturiers
seigneur.percevoir_impot()  # Le seigneur perçoit des impôts sur son noble vassal

# Affichage de l'état du seigneur, du noble et des roturiers
print(seigneur)
print(noble1)
print(roturier1)
print(roturier2)
