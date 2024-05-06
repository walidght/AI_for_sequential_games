import random
from strategies.Strategie import Strategie
from jeux.JeuSequentiel import JeuSequentiel

class StrategieOptimale(Strategie):
    """
    Représente une stratégie optimale basée sur la fonction de Grundy pour le jeu des allumettes.
    """

    def __init__(self, jeu: JeuSequentiel):
        super().__init__(jeu)
        self.valeurs_grundy = {}
	
	
    def precalculer_valeurs_grundy(self):
        """ Précalcule les valeurs de Grundy pour toutes les configurations possibles du jeu. """
        max_allumettes_per_group = max(self.jeu.allumettes)  # Trouve le nombre maximum d'allumettes dans un groupe
        self.valeurs_grundy = {}

        # Calcule les valeurs de Grundy pour toutes les configurations possibles
        def calculer_grundy(a):
            if a in self.valeurs_grundy:
                return self.valeurs_grundy[a]
            if a == 0:
                return 0  # Grundy(0) = 0

            seen_values = set()
            for x in range(1, a + 1):
                next_value = calculer_grundy(a - x)
                seen_values.add(next_value)

            # Trouve la plus petite valeur de Grundy non utilisée
            grundy = 0
            while grundy in seen_values:
                grundy += 1

            self.valeurs_grundy[a] = grundy
            return grundy

        for allumettes in self.generer_configurations_allumettes():
            valeur_grundy = 0
            for nb_allumettes in allumettes:
                valeur_grundy ^= calculer_grundy(nb_allumettes)
            self.valeurs_grundy[tuple(allumettes)] = valeur_grundy

	
    def generer_configurations_allumettes(self):
        """ Génère toutes les configurations possibles du jeu d'allumettes. """
        g = self.jeu.groupes
        m = self.jeu.allumettes[0]
        configurations = []

        def backtrack(configuration_actuelle):
            if len(configuration_actuelle) == g:
                configurations.append(list(configuration_actuelle))
                return
            for nb in range(m + 1):
                configuration_actuelle.append(nb)
                backtrack(configuration_actuelle)
                configuration_actuelle.pop()

        backtrack([])
        return configurations


    def choisirProchainCoup(self, C):
        """ Choisit le prochain coup optimal en utilisant la stratégie basée sur la fonction de Grundy. """
        if not self.valeurs_grundy:
            self.precalculer_valeurs_grundy()

        coups_possibles = self.jeu.coupsPossibles(C)
        for coup in coups_possibles:
            new_game = C.copy()
            self.jeu.joueLeCoup(new_game, coup)
            new_config = tuple(new_game.allumettes)
            if self.valeurs_grundy.get(new_config, -1) == 0:
                return coup
		
        # Si aucun coup ne réduit la valeur de Grundy à zéro, jouer un coup aléatoire
        return random.choice(coups_possibles)
