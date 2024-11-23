from .personne import Personne
from .roturier import Roturier
from typing import List

class Noble(Personne):
    """
    Classe représentant un noble, ayant des roturiers comme sujets et des villages sous son contrôle.
    """

    def __init__(self, nom: str, age: int, ressources: int, argent: int, bonheur: int, couleur: str = "green"):
        super().__init__(nom, age, ressources, argent, bonheur)
        self.villages = []  # Liste des villages contrôlés
        self.couleur = couleur

    def ajouter_village(self, village):
        """Ajoute un village sous le contrôle du noble."""
        village.couleur = self.couleur
        self.villages.append(village)
        
        print("ajouter village a ", self, "au coord : ", village.coords)

    def produire_ressources(self):
        """Appelle la production dans chaque village sous le contrôle du noble."""
        total = 0
        for village in self.villages:
            total += village.produire_ressources()
        self.ressources += total
        print(f"Production totale collectée par {self.nom} : {total}")

    def percevoir_impots(self):
        """Collecte les impôts de chaque village sous le contrôle du noble."""
        total_impots = sum(village.percevoir_impots() for village in self.villages)
        self.ressources += total_impots
        print(f"Impôts collectés par {self.nom} : {total_impots}")
        return total_impots

    def coord_village(self):
        return self.villages[0].coords
    
    def afficher_statut(self):
        """Affiche le statut du noble, de ses ressources et de ses villages."""
        print(f"Noble {self.nom} - Ressources : {self.ressources}, Bonheur : {self.bonheur}")
        print(f"Villages contrôlés : {len(self.villages)}")
        for village in self.villages:
            village.afficher_statut()
        print("")
