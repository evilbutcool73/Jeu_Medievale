from src.models import RecolteAbondante
from src.models import Epidemie
from src.models import Guerre
from src.models import Evenement

class GameController:
    def __init__(self):
        self.evenements = [
            RecolteAbondante(),
            Epidemie(),
            Guerre()
        ]

    def appliquer_evenements(self, personnages):
        """
        Applique des événements aléatoires à une liste de personnages.
        """
        for evenement in self.evenements:
            for personnage in personnages:
                if evenement.se_produit():
                    evenement.appliquer(personnage)
