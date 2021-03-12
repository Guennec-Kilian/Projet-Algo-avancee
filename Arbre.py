from copy import deepcopy
euroLib = ["c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8"]
euroTab = [200, 100, 50, 20, 10, 5, 2, 1]

class Arbre:
    """
        implémentation des arbres pour pouvoir chercher la solution optimal
        via les essais successifs
    """
    feuilles = []
    valeur = 0
    chemin = []

    def __init__(self, v_parent, chemin_parent, indicePiece):
        """
            Si indicePiece == -1, il s'agit d'une initialisation de l'arbre et non pas d'une feuille
        """
        if indicePiece != -1:
            self.valeur = v_parent + euroTab[indicePiece]
            self.chemin = chemin_parent
            self.chemin.append(euroLib[indicePiece])
            self.feuilles = []

    def addFeuille(self, indicePiece):
        self.feuilles.append(Arbre(self.valeur, deepcopy(self.chemin), indicePiece))
        
    def getSortedChemin(self):
        """
         pour pouvoir ensuite passer par une fonction d'affichage
        """
        s_chemin = deepcopy(self.chemin)
        s_chemin.sort()
        return s_chemin

    def isLower(self, limite):
        return self.valeur < limite

    def isEqual(self, limite):
        return self.valeur == limite

    def getLenChemin(self):
        return len(self.chemin)

    def affichage(self):
        subA = [f.affichage() for f in self.feuilles if self.feuilles != []]
        res = "<{0}, ".format(self.valeur)
        if subA != []:
            for a in subA:
                res += "{0}, ".format(a)
            return res[:-2] + ">"
        else:
             return res + ">"

if __name__ == "__main__":
    a = Arbre(0, [], -1)
    for k in range (len(euroLib)):
        a.addFeuille(k)
    a.feuilles[-1].addFeuille(3)

    print(a.affichage())