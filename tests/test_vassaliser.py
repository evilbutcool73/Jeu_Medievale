import sys
import os
import random
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.controllers.game_controller import GameController
from src.models.personnes import Roturier, Noble, Seigneur
from src.models.actions.guerre import Guerre
from src.models.actions.vassaliser import TentativeVassalisation  # Assurez-vous d'avoir cette classe dans le bon dossier

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

# Lancer plusieurs tours et déclencher une tentative de vassalisation entre Seigneur et Noble
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

    # Tentative de vassalisation entre seigneur1 et noble au tour 2
    if tour == 1:
        print("\n--- Tentative de Vassalisation ---")
        tentative_vassalisation = TentativeVassalisation(seigneur1, noble)
        tentative_vassalisation.tenter_vassalisation()
        
        # Afficher les conséquences de la tentative de vassalisation
        print(f"\nConséquences de la tentative de vassalisation:")
        print(seigneur1)
        print(noble)
