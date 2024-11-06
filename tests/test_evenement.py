import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.controllers.game_controller import GameController
from src.models.personnes import Roturier, Noble, Seigneur

# Créer des personnages
roturier = Roturier("Roturier Test", age=20, ressources=50, argent=20, bonheur=5, capacite_production=10)
noble = Noble("Noble Test", age=40, ressources=100, argent=50, bonheur=5)
seigneur = Seigneur("Seigneur Test", age=50, ressources=200, argent=100, bonheur=5)

noble.ajouter_roturier(roturier)
seigneur.ajouter_vassal(noble)

# Créer le contrôleur de jeu et ajouter des personnages
game_controller = GameController()

# Lancer plusieurs tours automatiquement
for tour in range(3):
    print(f"\n--- Tour {tour + 1} ---")
    game_controller.appliquer_evenements([roturier, noble, seigneur])  # Appliquer les événements
    roturier.produire()              # Production de ressources du roturier
    noble.percevoir_impot()           # Perception d'impôts par le noble
    seigneur.percevoir_impot()        # Perception d'impôts par le seigneur
    
    # Afficher l'état de chaque personnage après les événements et actions
    print(roturier)
    print(noble)
    print(seigneur)
