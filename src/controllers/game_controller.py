from src.models import Evenement
from src.models import RecolteAbondante
from src.models import Epidemie


# from src.models import GuerreCaracteristique

import random
from typing import List
from src.models import Seigneur

class GameController:
    def __init__(self):
        self.evenements = [
            RecolteAbondante(),
            Epidemie(),
            # Guerre()
        ]
    def appliquer_evenements(self, personnages):
        """
        Applique des événements aléatoires à une liste de personnages.
        """
        for evenement in self.evenements:
            for personnage in personnages:
                if evenement.se_produit():
                    evenement.appliquer(personnage)

    # def verifier_declenchement_guerre(self, seigneurs: List[Seigneur]):
    #     """Détermine si une guerre doit se déclencher entre deux seigneurs aléatoires."""
    #     if random.random() < 0.1:  # Exemple de probabilité de guerre
    #         attaquant = random.choice(seigneurs)
    #         defenseur = random.choice([s for s in seigneurs if s != attaquant])
    #         guerre = GuerreCaracteristique(attaquant, defenseur)
    #         self.guerres.append(guerre)
    #         guerre.declencher()  # Déclenche la guerre et applique les conséquences
