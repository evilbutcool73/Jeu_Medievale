class Personne:
    """
    Classe de base pour représenter une personne dans la société médiévale.
    """

    def __init__(self, nom: str, age: int, ressources: int, argent: int):
        self.nom = nom
        self.age = age
        self.ressources = ressources
        self.argent = argent

    def __str__(self):
        return (
            f"Nom : {self.nom}, "
            f"Âge : {self.age}, "
            f"Ressources : {self.ressources}, "
            f"Argent : {self.argent}"
        )
    def augmenter_ressources(self, montant: int):
        """Augmente les ressources de la personne de la valeur spécifiée."""
        self.ressources += montant

    def diminuer_ressources(self, montant: int):
        """Diminue les ressources de la personne de la valeur spécifiée, sans aller en dessous de zéro."""
        self.ressources = max(0, self.ressources - montant)

    def augmenter_argent(self, montant: int):
        """Augmente l'argent de la personne de la valeur spécifiée."""
        self.argent += montant

    def diminuer_argent(self, montant: int):
        """Diminue l'argent de la personne de la valeur spécifiée, sans aller en dessous de zéro."""
        self.argent = max(0, self.argent - montant)
