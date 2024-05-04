import random
from strategies.Strategie import Strategie
from jeux.JeuSequentiel import JeuSequentiel


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
        coups_possibles = self.jeu.coupsPossibles(C)  # Récupère les coups possibles
        
        # Choix aléatoire d'un coup parmi les coups possibles
        return random.choice(coups_possibles)
