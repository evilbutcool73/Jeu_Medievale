import sys
import os
import random
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.controllers.game_controller import GameController
from src.models.personnes import Roturier, Noble, Seigneur
from src.models.actions.guerre import Guerre

# Créer des personnages
roturier = Roturier("Roturier Test", age=20, ressources=50, argent=20, bonheur=5, capacite_production=10)
noble = Noble("Noble Test", age=40, ressources=100, argent=50, bonheur=5)
seigneur1 = Seigneur("Seigneur A", age=50, ressources=200, argent=100, bonheur=5)
seigneur2 = Seigneur("Seigneur B", age=55, ressources=180, argent=90, bonheur=5)

# Ajouter des relations de vassalité
noble.ajouter_roturier(roturier)
seigneur1.ajouter_vassal(noble)

# Instancier le contrôleur de jeu
game_controller = GameController()

# Lancer plusieurs tours et déclencher une guerre entre deux seigneurs
for tour in range(3):
    print(f"\n--- Tour {tour + 1} ---")
    
    # Appliquer les événements aléatoires
    game_controller.appliquer_evenements([roturier, noble, seigneur1, seigneur2])
    
    # Production de ressources et perception d'impôts
    roturier.produire()          # Le roturier produit des ressources
    noble.percevoir_impot()       # Le noble perçoit des impôts de ses roturiers
    seigneur1.percevoir_impot()   # Le seigneur perçoit des impôts de ses vassaux

    # Afficher l'état de chaque personnage
    print(roturier)
    print(noble)
    print(seigneur1)
    print(seigneur2)

    # Déclencher une guerre entre seigneur1 et seigneur2 au tour 2
    if tour == 1:
        print("\n--- Guerre entre Seigneur A et Seigneur B ---")
        guerre = Guerre(seigneur1, seigneur2)
        guerre.declencher()
        
        # Afficher les conséquences de la guerre
        print(f"\nConséquences de la guerre entre {seigneur1.nom} et {seigneur2.nom}:")
        print(seigneur1)
        print(seigneur2)
