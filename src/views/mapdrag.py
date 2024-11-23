class MapDrag:
    def __init__(self, canvas, map_manager):
        self.canvas = canvas
        self.map_manager = map_manager  # Référence pour gérer les compensateurs
        self.debut_x = 0
        self.debut_y = 0

        # Activer les bindings pour le drag
        self.canvas.bind("<ButtonPress-3>", self.sur_map_click_droit)
        self.canvas.bind("<B3-Motion>", self.sur_map_drag)

    def sur_map_click_droit(self, event):
        self.debut_x = event.x
        self.debut_y = event.y

    def sur_map_drag(self, event):
        dx = (event.x - self.debut_x) // self.map_manager.cell_size
        dy = (event.y - self.debut_y) // self.map_manager.cell_size

        # Sensibilité pour limiter les petits déplacements
        sensibilite = 1
        if dx > sensibilite :
            dx = 1
            self.debut_x, self.debut_y = event.x, event.y
        elif dx < -sensibilite :
            dx = -1
            self.debut_x, self.debut_y = event.x, event.y
        else :
            dx = 0
        if dy > sensibilite :
            dy = 1
            self.debut_x, self.debut_y = event.x, event.y
        elif dy < -sensibilite:
            dy = -1
            self.debut_x, self.debut_y = event.x, event.y
        else:
            dy = 0
        # Calculer les nouveaux compensateurs
        nouveau_compenser_x = self.map_manager.map_compenser_x - dx
        nouveau_compenser_y = self.map_manager.map_compenser_y - dy

        # Limiter les compensateurs aux bornes de la carte
        max_compenser_x = len(self.map_manager.map.grid[0]) - self.map_manager.nb_colonnes_visibles
        max_compenser_y = len(self.map_manager.map.grid) - self.map_manager.nb_lignes_visibles

        nouveau_compenser_x = max(min(nouveau_compenser_x, max_compenser_x), 0)
        nouveau_compenser_y = max(min(nouveau_compenser_y, max_compenser_y), 0)

        if (nouveau_compenser_x != self.map_manager.map_compenser_x or
                nouveau_compenser_y != self.map_manager.map_compenser_y):
            self.map_manager.map_compenser_x = nouveau_compenser_x
            self.map_manager.map_compenser_y = nouveau_compenser_y
            self.map_manager.dessiner_map_visible()
