from strategies.Strategie import Strategie
from jeux.JeuSequentiel import JeuSequentiel


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
        coups_possibles = self.jeu.coupsPossibles(C)  # Récupère les coups possibles

        meilleur_coup = None

        est_maximisant = True if self.jeu.joueurCourant(C) == "X" else False

        if est_maximisant:
            meilleur_score = float('-inf')
        else:
            meilleur_score = float('inf')

        for coup in coups_possibles:
            new_game = C.copy()

            # Joue le coup dans la configuration C
            self.jeu.joueLeCoup(new_game, coup)
            if est_maximisant:
                # Appelle la fonction minimax pour évaluer le score
                score = self.minimax(new_game, False, self.k)
                if score > meilleur_score:
                    meilleur_score = score
                    meilleur_coup = coup
            else:
                # Appelle la fonction minimax pour évaluer le score
                score = self.minimax(new_game, True, self.k)
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
                new_c = C.copy()
                self.jeu.joueLeCoup(new_c, coup)
                score = self.minimax(new_c, False, depth - 1)
                meilleur_score = max(meilleur_score, score)
            return meilleur_score
            
        else:
            meilleur_score = float('inf')
            for coup in self.jeu.coupsPossibles(C):
                new_c = C.copy()
                self.jeu.joueLeCoup(new_c, coup)
                score = self.minimax(new_c, True, depth - 1)
                meilleur_score = min(meilleur_score, score)
            return meilleur_score
