from ...views.generationmap import Map
from ...views.Type import TYPE

class AcheterCase:
    def __init__(self, jeu_interface, prix_case = 1):
        self.jeu_interface = jeu_interface
        self.prix_case = prix_case  # Prix d'une case

    def acheter_case(self, x, y, joueur, mode_achat):
        """Permet au joueur d'acheter une case si le joueur a suffisamment d'argent et si la case est voisine d'un de ses villages."""
        if joueur.argent >= self.prix_case:
            # Vérifier si la case peut être achetée
            case = self.jeu_interface.map.grid[y][x]

            # Vérifier si la case n'est pas un village et si elle n'est pas déjà possédée
            if case.type != TYPE.village and case.villageproprio is None:
                # Vérifier si la case est voisine d'un village du joueur
                if self.est_voisine_village(x, y, joueur):
                    # Effectuer l'achat : diminuer l'argent du joueur et marquer la case comme possédée
                    joueur.argent -= self.prix_case
                    case.villageproprio = joueur.villages[0]  # Associer la propriété au village du joueur
                    self.jeu_interface.mettre_a_jour_infos()  # Mettre à jour les informations d'affichage
                    print(f"Case à ({x}, {y}) achetée avec succès !")
                    if joueur.argent == 0:
                        mode_achat.set(False)
                else:
                    print(f"La case à ({x}, {y}) n'est pas voisine d'un de vos villages.")
            else:
                print(f"La case à ({x}, {y}) ne peut pas être achetée.")
        else:
            print("Vous n'avez pas assez d'argent pour acheter cette case.")

    def est_voisine_village(self, x, y, joueur):
        """Vérifie si la case à (x, y) est voisine d'un des villages du joueur."""
        # Vérifier les 8 cases voisines autour de la case (x, y)
        voisins = [
                    (0, -1),   # Lignes au-dessus
            (-1, 0),        (1, 0),      # Lignes au même niveau
                    (0, 1),        # Lignes en dessous
        ]
        
        for dx, dy in voisins:
            nx, ny = x + dx, y + dy
            
            # Vérifier si les coordonnées sont dans les limites de la carte
            if 0 <= nx < len(self.jeu_interface.map.grid[0]) and 0 <= ny < len(self.jeu_interface.map.grid):
                case_voisine = self.jeu_interface.map.grid[ny][nx]
                # Vérifier si la case voisine appartient à un des villages du joueur
                if case_voisine.villageproprio and case_voisine.villageproprio in joueur.villages:
                    return True
        return False
