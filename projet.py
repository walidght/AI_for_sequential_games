from jeux.Morpion import Morpion
from jeux.Allumettes import Allumettes


def executer_partie_morpion(jeu, strategie1, strategie2):
    """Exécute une partie de morpion entre deux joueurs utilisant la stratégie aléatoire.
    @param strategie1 (Strategie): La première stratégie de jeu.
    @param strategie2 (Strategie): La deuxième stratégie de jeu.
    @return symbole_gagnant (str): Le symbole du joueur gagnant ('X' ou 'O'), ou '' en cas de match nul.
    """

    # Boucle principale de jeu
    while not Morpion.estFini(jeu):
        # Récupère le symbole du joueur courant
        joueur_courant = Morpion.joueurCourant(jeu)

        # Choix du coup en fonction de la stratégie du joueur courant
        if joueur_courant == 'X':
            coup = strategie1.choisirProchainCoup(jeu)
        else:
            coup = strategie2.choisirProchainCoup(jeu)

        Morpion.joueLeCoup(jeu, coup)  # Le joueur courant joue le coup choisi

        Morpion.afficherConfig(jeu)

    # Détermination du gagnant ou match nul
    if Morpion.victoire(jeu, 'X'):
        return 'X'
    elif Morpion.victoire(jeu, 'O'):
        return 'O'
    else:
        return ''


def executer_partie_allumettes(jeu, strategie1, strategie2):
    """Exécute une partie d'allumettes entre deux joueurs utilisant de strategie.
    @param strategie1 (Strategie): La stratégie de premier joueur.
    @param strategie2 (Strategie): La stratégie de deuxième joueur.
    @return symbole_gagnant (int): Le joueur gagnant (1 ou 2)
    """

    # Boucle principale de jeu
    while not Allumettes.estFini(jeu):
        # Récupère le symbole du joueur courant
        joueur_courant = Allumettes.joueurCourant(jeu)

        # Choix du coup en fonction de la stratégie du joueur courant
        if joueur_courant == 1:
            coup = strategie1.choisirProchainCoup(jeu)
        else:
            coup = strategie2.choisirProchainCoup(jeu)

        # Le joueur courant joue le coup choisi
        Allumettes.joueLeCoup(jeu, coup)

        Allumettes.afficherConfig(jeu)

    # Détermination du gagnant ou match nul
    if Allumettes.victoire(jeu, 1):
        return 1
    elif Allumettes.victoire(jeu, 2):
        return 2
    else:
        return 0
