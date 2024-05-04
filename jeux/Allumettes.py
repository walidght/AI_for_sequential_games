import time
from IPython.display import clear_output
from jeux.JeuSequentiel import JeuSequentiel


class Allumettes(JeuSequentiel):
    """
    Représente le jeu des allumettes avec g groupes de m allumettes chacun.
    """

    def __init__(self, g: int, m: int):
        super().__init__()
        self.groupes = g
        self.allumettes = [m] * g  # Initialise chaque groupe avec m allumettes
        self.tour = 0  # Initialise le tour de jeu

    def copy(self):
        new_game = Allumettes(self.groupes, self.allumettes[0])
        new_game.allumettes = self.allumettes.copy()
        new_game.tour = self.tour
        return new_game

    @staticmethod
    def afficherConfig(C):
        """
        Affiche la configuration C.
        """
        clear_output(wait=True)  # Clear the output without scrolling
        for i, nb_allumettes in enumerate(C.allumettes):
            print(f"Groupe {i+1}: {nb_allumettes} allumettes")
        time.sleep(1)  # Simulate some processing time

    @staticmethod
    def joueurCourant(C):
        """
        Rend le joueur courant dans la configuration C.
        Dans ce jeu, les joueurs jouent à tour de rôle.
        """
        return 1 if C.tour % 2 == 0 else 2


    @staticmethod
    def coupsPossibles(C):
        """
        Rend la liste des coups possibles dans la configuration C.
        Un coup possible consiste à choisir un groupe avec au moins une allumette.
        """
        return [(i, j) for i, nb_allumettes in enumerate(C.allumettes) if nb_allumettes > 0 for j in range(1, nb_allumettes + 1)]

    @staticmethod
    def joueLeCoup(C, coup):
        """
        Modifie la configuration C en jouant le coup donné.
        """
        groupe, nb_allumettes = coup
        # Retire les allumettes du groupe choisi
        C.allumettes[groupe] -= nb_allumettes
        C.tour += 1  # Incrémente le tour de jeu

    @staticmethod
    def estFini(C):
        """
        Rend True si la configuration C est une configuration finale.
        Dans ce jeu, la configuration finale est atteinte lorsque toutes les allumettes ont été retirées.
        """
        return all(nb == 0 for nb in C.allumettes)
    
    @staticmethod
    def victoire(C, joueur):
        """
        Rend True si le joueur donné a gagné la partie.
        """
        joueur = 0 if joueur == 2 else 1
        return C.estFini(C) and C.tour % 2 == joueur 
    
    @staticmethod
    def f1(C):
        """
        Rend la valeur de l'évaluation de la configuration C pour le joueur 1.
        Dans ce jeu, on peut simplement retourner 1 si le joueur 1 gagne et -1 s'il perd.
        """
        return 1 if C.estFini(C) and C.tour % 2 == 1 else -1
