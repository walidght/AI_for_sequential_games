import copy
import time
from IPython.display import clear_output
from jeux.JeuSequentiel import JeuSequentiel


class Morpion(JeuSequentiel):
    """
    Représente le jeu du morpion (3x3).
    """

    def __init__(self):
        # Initialisation de la grille vide
        self.grille = [[' ']*3 for _ in range(3)]
        self.last_turn = None

    @staticmethod
    def joueurCourant(C):
        # Compte le nombre de 'X' et de 'O' dans la grille pour déterminer le joueur courant
        nb_X = sum(row.count('X') for row in C.grille)
        nb_O = sum(row.count('O') for row in C.grille)
        return 'X' if nb_X <= nb_O else 'O'

    @staticmethod
    def coupsPossibles(C):
        coups = []	# Liste des coups possibles
        for i in range(3):
            for j in range(3):
                if C.grille[i][j] == ' ':	# Si la case est vide
                    coups.append((i, j)) 	# Ajoute le coup possible
        return coups

    @staticmethod
    def f1(C):
        # Évaluation du jeu pour le joueur 'X' (joueur 1)
        if Morpion.victoire(C, 'X'):
            return 1
        elif Morpion.victoire(C, 'O'):
            return -1
        else:
            return 0  # Match nul

    @staticmethod
    def joueLeCoup(C, coup):
        i, j = coup
        C.grille[i][j] = Morpion.joueurCourant(C)
        C.last_turn = coup

    @staticmethod
    def estFini(C):
        # Vérifie s'il y a un gagnant ou si la grille est pleine (match nul)
        return Morpion.victoire(C, 'X') or Morpion.victoire(C, 'O') or ' ' not in [cell for row in C.grille for cell in row]

    @staticmethod
    def victoire(C, symbole):
        # Vérifie si le joueur avec le symbole donné a gagné
        for i in range(3):
            if all(C.grille[i][j] == symbole for j in range(3)):
                return True		# Victoire sur la ligne i
            if all(C.grille[j][i] == symbole for j in range(3)):
                return True		# Victoire sur la colonne i
        if all(C.grille[i][i] == symbole for i in range(3)):
            return True			# Victoire sur la diagonale principale
        if all(C.grille[i][2 - i] == symbole for i in range(3)):
            return True			# Victoire sur la diagonale secondaire
        return False 			# Aucune victoire

    @staticmethod
    def afficherConfig(C):
        """
        Affiche la configuration C.
        """
        clear_output(wait=True)	 # Effacer la sortie sans faire défiler
        for row in C.grille:
            print(' | '.join(row))
            print('---------')
        time.sleep(1)  # Simulez un temps de traitement

    def copy(self):
        new_game = Morpion()
        new_game.grille = copy.deepcopy(self.grille)
        new_game.last_turn = self.last_turn
        return new_game
