# Compte Rendu du Projet "La Guerre des Frontières"

## Introduction

Ce document présente l'architecture du projet "La Guerre des Frontières", un jeu médiéval basé sur le modèle MVC. Ce projet explore la simulation d'un univers où les interactions entre personnages influencent le déroulement du jeu.

---

## Table des matières

1. [Objectifs](#objectifs)  
2. [Ce qui a été fait / non fait](#ce-qui-a-été-fait--non-fait)  
3. [Qualités Ergonomiques de l’IHM](#qualités-ergonomiques-de-lihm)  
4. [Structure du Projet](#structure-du-projet)  
   - [Organisation des Classes](#organisation-des-classes)  
   - [Relations entre les Classes](#relations-entre-les-classes)  
   - [Diagramme UML](#diagramme-uml)  
5. [Méthodologie](#méthodologie)  
6. [Conclusion](#conclusion)  
7. [Annexes](#annexes)  

---

## Objectifs

Créer une architecture modulaire et extensible qui facilite la gestion des entités et des interactions.

Mettre en avant une IHM ergonomique respectant des principes de cohérence, flexibilité, et retour d’informations.

Créer un jeu amusant et engageant !

---

## Ce qui a été fait / non fait

- **Fonctionnalités implémentées :**
  - Création des classes principales (`Personne`, `Roturier`, `Noble`, etc.).
  - Gestion des relations entre les entités (héritage, composition).
  - Prototype d’IHM simple permettant l’interaction de base avec le jeu.

- **Limitations :**
  - Les bots disposent d’une IA semi-avancée.
  - La gestion du bonheur des personnages n'est pas encore implémentée.

---

## Qualités Ergonomiques de l’IHM

- **Cohérence :** L’IHM conserve des couleurs, des boutons et des icônes uniformes.
- **Concision :** Les joueurs interagissent via des boutons simples et des menus clairs (pas plus de 3 clics pour atteindre une action souhaitée).
- **Structuration des activités :** Les étapes principales (sélection, action, confirmation) sont guidées par des dialogues.
- **Flexibilité :** Les actions récurrentes peuvent être effectuées avec la souris ou des raccourcis clavier.
- **Retour d’informations :** L’IHM affiche des messages pour valider les actions (ex. : "Village conquis").
- **Gestion des erreurs :** Les erreurs utilisateur sont signalées par des messages (ex. : "Erreur de sauvegarde") et gérées via des blocs `try` et `except`.

---

## Structure du Projet

### Organisation des Classes

Voici les principales classes du projet :

- Personne : Classe de base représentant un individu.

- Roturier : Hérite de Personne, représentant une classe sociale plus modeste.

- Paysan : Hérite de Roturier, un roturier spécialisé dans l'agriculture.

- Noble : Hérite de Personne, capable de posséder des armées et des villages.

- Seigneur : Hérite de Noble, chef suprême possédant des vassaux.

- Soldat : Classe indépendante représentant une unité militaire.

- Village : Regroupe des habitants et appartient à un noble.

- Fief : Regroupe plusieurs villages.

- Evenement : Classe de base pour modéliser les événements comme les récoltes abondantes ou les épidémies.

- GameController : Classe centrale gérant les interactions entre les différentes entités du jeu.

### Relations entre les Classes :
- Les relations entre ces classes sont définies de manière hiérarchique ou par composition. Les nobles, par exemple, possèdent des villages, et les seigneurs peuvent tenter de vassaliser d'autres nobles.

### Diagramme UML
- Le diagramme UML ci-dessous illustre les relations entre les différentes classes du projet :
    ![UML PROJET](./Rendu/plantUML.png)
    ### Description du Graphe de Classes

    Le diagramme UML illustre les relations suivantes :

    **Héritage :**
    - Personne est la classe de base pour Roturier et Noble.
    - Roturier est spécialisée par Paysan, et Noble par Seigneur.

    **Composition :**
    - Un Noble possède un ou plusieurs Villages.
    - Un Fief regroupe plusieurs Villages.

    Ces relations respectent les principes de modularité et facilitent l'extension du projet (ajout de nouvelles classes comme Marchand ou Artisan).

---

## Méthodologie

**Étapes Réalisées :**

1. Analyse des besoins : Identification des entités principales et des interactions nécessaires.
2. Modélisation UML : Création d’un diagramme clair représentant l'architecture.
3. Implémentation des classes : Développement des classes en Python selon le diagramme défini.
4. Documentation : Rédaction de ce compte rendu.

**Outils Utilisés :**

- `Python` : Langage principal pour le développement.
- `PlantUML` : Description graphique de l’architecture du projet.  

---

## Conclusion

Le projet "La Guerre des Frontières" offre une structure claire et modulable, facilitant l'ajout de nouvelles fonctionnalités. Le diagramme UML permet de visualiser efficacement les relations complexes entre les différentes entités. Ce compte rendu servira de référence pour toute évolution du projet.

---

## Annexes

Fichier PlantUML (.puml) : Code source pour le diagramme UML (disponible dans le folder Rendu).
