from .personne import Personne
from .roturier import Roturier
from typing import List

class Noble(Personne):
    """
    Classe représentant un noble, ayant des roturiers comme sujets.
    """

    def __init__(self, nom: str, age: int, ressources: int, argent: int):
        super().__init__(nom, age, ressources, argent)
        self.roturiers: List[Roturier] = []

    def ajouter_roturier(self, roturier: Roturier):
        """Ajoute un roturier à la liste des roturiers du noble."""
        self.roturiers.append(roturier)

    def percevoir_impot(self):
        """
        Perçoit un impôt en prenant une part des ressources de chaque roturier.
        """
        for roturier in self.roturiers:
            impots = roturier.ressources * 0.2  # Par exemple, le noble prend 50 % des ressources du roturier
            roturier.diminuer_ressources(impots)
            self.augmenter_ressources(impots)

    def __str__(self):
        return (
            super().__str__() +
            f", Type : Noble, "
            f"Nombre de roturiers : {len(self.roturiers)}"
        )