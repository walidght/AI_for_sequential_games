import random
from IPython.display import clear_output
import time
import copy


class JeuSequentiel:
    """
    Represente un jeu sequentiel, a somme
    nulle, a information parfaite
    """

    def __init__(self):
        pass

    @staticmethod
    def joueurCourant(C):
        """
        Rend le joueur courant dans la
        configuration C
        """
        raise NotImplementedError

    @staticmethod
    def coupsPossibles(C):
        """
        Rend la liste des coups possibles dans
        configuration C
        """
        raise NotImplementedError

    @staticmethod
    def f1(C):
        """
        Rend la valeur de l'evaluation de la
        configuration C pour le joueur 1
        """
        raise NotImplementedError

    @staticmethod
    def joueLeCoup(C, coup):
        """
        Rend la configuration obtenue apres
        que le joueur courant ait joue le coup
        dans la configuration C
        """
        raise NotImplementedError

    @staticmethod
    def estFini(C):
        """
        Rend True si la configuration C est
        une configuration finale
        """
        raise NotImplementedError

    @staticmethod
    def annuleDernierCoup(C):
        """
        Annule le dernier coup joué dans la configuration C.
        """
        raise NotImplementedError


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
        coups = []  # Liste des coups possibles
        for i in range(3):
            for j in range(3):
                if C.grille[i][j] == ' ':  # Si la case est vide
                    coups.append((i, j))  # Ajoute le coup possible
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
                return True  # Victoire sur la ligne i
            if all(C.grille[j][i] == symbole for j in range(3)):
                return True  # Victoire sur la colonne i
        if all(C.grille[i][i] == symbole for i in range(3)):
            return True  # Victoire sur la diagonale principale
        if all(C.grille[i][2 - i] == symbole for i in range(3)):
            return True  # Victoire sur la diagonale secondaire
        return False  # Aucune victoire

    @staticmethod
    def annuleDernierCoup(C):
        """
        Annule le dernier coup joué dans la configuration C.
        """
        if not C.last_turn:
            return
        i, j = C.last_turn
        C.grille[i][j] = ' '  # Réinitialise la case du dernier coup joué
        C.last_turn = None  # Réinitialise le dernier coup joué

    @staticmethod
    def afficherConfig(C):
        """
        Affiche la configuration C.
        """
        clear_output(wait=True)  # Clear the output without scrolling
        for row in C.grille:
            print(' | '.join(row))
            print('---------')
        time.sleep(1)  # Simulate some processing time


class Strategie:
    """
    Représente une stratégie de jeu.
    """

    def __init__(self, jeu: JeuSequentiel):
        self.jeu = jeu

    def choisirProchainCoup(C):
        """
        Choisit un coup parmi les coups possibles dans la configuration C.
        """
        raise NotImplementedError


class StrategieAleatoire(Strategie):
    """
    Représente une stratégie de jeu aléatoire pour tout jeu séquentiel.
    """

    def __init__(self, jeu: JeuSequentiel):
        super().__init__(jeu)

    def choisirProchainCoup(self, C):
        """
        Choisit un coup aléatoire suivant une distribution uniforme sur tous les coups
        possibles dans la configuration C.
        """
        coups_possibles = self.jeu.coupsPossibles(
            C)  # Récupère les coups possibles
        # Choix aléatoire d'un coup parmi les coups possibles
        return random.choice(coups_possibles)


def executer_partie_morpion(jeu, strategie1, strategie2):
    """Exécute une partie de morpion entre deux joueurs utilisant la stratégie aléatoire.
    @param strategie1 (Strategie): La première stratégie de jeu.
    @param strategie2 (Strategie): La deuxième stratégie de jeu.
    @return symbole_gagnant (str): Le symbole du joueur gagnant ('X' ou 'O'), ou ' ' en cas de match nul.
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
        return ' '  # Match nul


class StrategieMinMax(Strategie):
    """
    Représente une stratégie de jeu basée sur l'algorithme Minimax pour tout jeu séquentiel.
    """

    def __init__(self, jeu: JeuSequentiel, k):
        super().__init__(jeu)
        self.k = k

    def choisirProchainCoup(self, C):
        """
        Choisit le meilleur coup possible en utilisant l'algorithme Minimax dans la configuration C.
        """

        coups_possibles = self.jeu.coupsPossibles(
            C)  # Récupère les coups possibles

        meilleur_coup = None

        est_maximisant = True if self.jeu.joueurCourant(C) == "X" else False

        if est_maximisant:
            meilleur_score = float('-inf')
        else:
            meilleur_score = float('inf')

        for coup in coups_possibles:
            new_game = Morpion()
            new_game.grille = copy.deepcopy(C.grille)
            new_game.last_turn = C.last_turn

            # Joue le coup dans la configuration C
            self.jeu.joueLeCoup(new_game, coup)
            if est_maximisant:
                # Appelle la fonction minimax pour évaluer le score
                score = self.minimax(new_game, True, self.k)
                if score > meilleur_score:
                    meilleur_score = score
                    meilleur_coup = coup
            else:
                # Appelle la fonction minimax pour évaluer le score
                score = self.minimax(new_game, False, self.k)
                if score < meilleur_score:
                    meilleur_score = score
                    meilleur_coup = coup

        return meilleur_coup

    def minimax(self, C, est_maximisant, depth):
        """
        Algorithme Minimax pour évaluer la configuration C.
        """
        if self.jeu.estFini(C) or depth == 0:
            return self.jeu.f1(C)

        if est_maximisant:
            meilleur_score = float('-inf')
            for coup in self.jeu.coupsPossibles(C):
                self.jeu.joueLeCoup(C, coup)
                score = self.minimax(C, False, depth - 1)
                meilleur_score = max(meilleur_score, score)
                self.jeu.annuleDernierCoup(C)
            return meilleur_score
        else:
            meilleur_score = float('inf')
            for coup in self.jeu.coupsPossibles(C):
                self.jeu.joueLeCoup(C, coup)
                score = self.minimax(C, True, depth - 1)
                meilleur_score = min(meilleur_score, score)
                self.jeu.annuleDernierCoup(C)
            return meilleur_score
