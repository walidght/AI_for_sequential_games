from jeux.JeuSequentiel import JeuSequentiel


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