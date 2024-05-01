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
    def copy(self):
        """
        Creates a deep copy of the current game configuration.
        """
        raise NotImplementedError
