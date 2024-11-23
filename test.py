import tkinter as tk

def on_space_press(event):
    print("La barre d'espace a été pressée!")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Exemple Bind Barre Espace")

# Lier la barre d'espace
root.bind("<space>", on_space_press)

# Lancer la boucle principale
root.mainloop()