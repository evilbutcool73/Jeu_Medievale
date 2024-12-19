# main.py
import tkinter as tk
from src.views import MenuPrincipal 

def main():

    # Lancement de l'application
    root = tk.Tk()
    MenuPrincipal(root)
    root.mainloop()

if __name__ == "__main__":
    main()