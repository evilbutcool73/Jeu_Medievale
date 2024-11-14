import tkinter as tk
from tkinter import font
from ..models import *
from ..controllers import *

class JeuInterface:
    def __init__(self, root, main_frame, game_controller):
        self.root = root
        self.main_frame = main_frame
        self.gamecontroller = game_controller
        self.root.title("Jeu Médiéval")
        self.root.geometry("800x600")
        self.root.configure(bg="#2E2E2E")
        self.root.resizable(True, True)
        self.action_selectionnee = None

        # Cadre pour l'affichage des informations en haut
        self.info_frame = tk.Frame(self.main_frame, height=50, bg="#3A3A3A")
        self.info_frame.pack(fill="x", pady=(10, 5))
        self.afficher_informations()

        # Cadre pour la carte (grille)
        self.map_frame = tk.Frame(self.main_frame, bg="#2E2E2E")
        self.map_frame.pack(expand=True, fill="both", padx=20, pady=10)
        self.creer_grille_carte()

        # Cadre pour les actions en bas
        self.actions_frame = tk.Frame(self.main_frame, height=50, bg="#3A3A3A")
        self.actions_frame.pack(fill="x", pady=(5, 10))
        self.afficher_actions()
        self.tour_suivant()

    def afficher_informations(self):
        label_font = font.Font(family="Helvetica", size=14, weight="bold")
        self.argent_label = tk.Label(self.info_frame, text=f"Argent : {self.gamecontroller.joueur.argent}", bg="#3A3A3A", fg="#F7F7F7", font=label_font)
        self.argent_label.pack(side="left", padx=15)
        self.ressources_label = tk.Label(self.info_frame, text=f"Ressources : {self.gamecontroller.joueur.ressources}", bg="#3A3A3A", fg="#F7F7F7", font=label_font)
        self.ressources_label.pack(side="left", padx=15)
    
    def mettre_a_jour_infos(self):
        """Met à jour l'interface avec les infos actuelles du jeu."""
        # Accède aux informations du joueur et du village depuis `etat_du_jeu`
        self.argent_label.config(text=f"Argent : {self.gamecontroller.joueur.argent}")
        self.ressources_label.config(text=f"Ressources : {self.gamecontroller.joueur.ressources}")

    def creer_grille_carte(self):
        self.canvas = tk.Canvas(self.map_frame, bg="#2E2E2E", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        rows, cols = 10, 10
        cell_size = 50
        for i in range(rows):
            for j in range(cols):
                x1, y1 = j * cell_size, i * cell_size
                x2, y2 = x1 + cell_size, y1 + cell_size
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="#474747", fill="#3A3A3A")

    def afficher_actions(self):
        button_font = font.Font(family="Helvetica", size=12, weight="bold")
        self.impot_bouton = tk.Button(
            self.actions_frame,
            text="Impot",
            command=lambda: self.selectionner_action("impot"),
            font=button_font,
            bg="#1C6E8C",
            fg="white",
            activebackground="#145374",
            activeforeground="white",
            bd=0,
            padx=20,
            pady=5
        )
        self.impot_bouton.pack(side="left", padx=15)
    
    def selectionner_action(self,action):
        if self.action_selectionnee == action:
            self.action_selectionnee = None
            self.reset_bouton_couleurs()
        else:
            self.action_selectionnee = action
            self.reset_bouton_couleurs()
            if action == "impot":
                self.impot_bouton.config(bg="#3498DB")

    def reset_bouton_couleurs(self):
        self.impot_bouton.config(bg="#1C6E8C")

    def tour_suivant(self):
        button_font = font.Font(family="Helvetica", size=12, weight="bold")
        self.tour_suivant_bouton = tk.Button(
            self.actions_frame,
            text="Valider/Tour Suivant",
            command=self.executer_action_selectionnee,
            font=button_font,
            bg="#1C6E8C",
            fg="white",
            activebackground="#145374",
            activeforeground="white",
            bd=0,
            padx=20,
            pady=5
        )
        self.tour_suivant_bouton.pack(side="right", padx=15)
        print(self.gamecontroller.village_joueur.afficher_statut())
    
    def executer_action_selectionnee(self):
        #print("oui")
        if self.action_selectionnee == "impot":
            
            self.gamecontroller.joueur.percevoir_impots()
            print("Action exécutée: Produire des ressources")
            self.gamecontroller.appliquer_evenements(self.gamecontroller.village_joueur.habitants)
            self.mettre_a_jour_infos()

        self.action_selectionnee = None
        self.reset_bouton_couleurs()
        self.mettre_a_jour_infos()
        print(self.gamecontroller.joueur.argent)

        