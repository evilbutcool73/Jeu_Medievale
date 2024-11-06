import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.controllers.game_controller import GameController
from src.models import Personne,Roturier, Paysan, Noble, Seigneur

# Création de personnages
roturier1 = Roturier("Roturier 1", age=20, ressources=50, argent=50, capacite_production=10)
noble1 = Noble("Noble 1", age=40, ressources=100, argent=50)

# Instanciation du contrôleur de jeu
game_controller = GameController()

# Appliquer des événements aléatoires
game_controller.appliquer_evenements([roturier1, noble1])

print(roturier1)
print(noble1)
