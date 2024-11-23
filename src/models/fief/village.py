from src.models import *

class Village:
        
    def __init__(self, nom, coords, couleur: str = "green" ):
        self.nom = nom
        self.habitants = []  # Liste d'instances de Roturier et de Paysan
        self.coords = coords
        self.couleur = couleur

    def ajouter_habitant(self, habitant):
        """Ajoute un habitant au village."""
        self.habitants.append(habitant)

    @property
    def population(self):
        return len(self.habitants)

    def produire_ressources(self):
        """Calcule la production totale des habitants."""
        production_totale = sum(habitant.produire() for habitant in self.habitants)
        print(f"Production totale dans {self.nom} : {production_totale}")
        return production_totale

    def percevoir_impots(self):
        """Calcule les impôts perçus en fonction du type d'habitant."""
        total_impots = 0
        for habitant in self.habitants:
            if isinstance(habitant, Paysan):
                impots = int(habitant.ressources * 0.5)  # 50% pour les paysans
            elif isinstance(habitant, Roturier):
                impots = int(habitant.ressources * 0.25)  # 25% pour les roturiers
            else:
                impots = 0
            habitant.diminuer_ressources(impots)  # Soustraire les impôts de la richesse de l'habitant
            total_impots += impots
        print(f"Impôts perçus dans {self.nom} : {total_impots}")
        return total_impots

    def afficher_statut(self):
        """Affiche les informations générales et de chaque habitant."""
        print(f"Village {self.nom} - Population : {self.population}")
        for habitant in self.habitants:
            print(f"{habitant.nom} - Ressources : {habitant.ressources}, Richesse : {habitant.argent}, Bonheur : {habitant.bonheur}")
        print("")
