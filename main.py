﻿import Arbre

A = Arbre.Arbre
euroLib = ["c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8"]
euroTab = [200, 100, 50, 20, 10, 5, 2, 1]


def listCounter(listC):
    varList = [[],[]]
    #varList[0] contient les pieces cX
    #varList[1] contient le nombre de fois que chaque vpiece apparait
    for k in range (len(listC)):
        if (listC[k] not in varList[0]):
            varList[0].append(listC[k])
            varList[1].append(1)
        else :
            i = 0
            flag = 0
            while (i < len(varList[0]) and flag!=1):
                
                if (varList[0][i]==listC[k]):
                    varList[1][i]+=1
                    flag = 1
                i+=1
    #Affichage 
    for k in range (len(varList[0])) :
        print("La piece {0} apparait {1} fois".format(varList[0][k],varList[1][k]))

def essaiSucc(a, N, solution):
    # a le noeud que l'on traite
    # N la valeur a atteindre
    for k in range (len(euroLib)):
        a.addFeuille(k)
    
    for x in a.feuilles:
        if x.isEqual(N):
            if len(solution) == 0 or len(solution) > x.getLenChemin():
                solution = x.getSortedChemin()
        elif x.isLower(N):
            essaiSucc(x, N, solution)
        

def glouton(aRendre):
    pieces =  []
    troubleshout = 0
    while aRendre != 0:
        searching = True
        i = 0
        while searching and i < len(euroLib):
            if aRendre >= euroTab[i]:
                # si le reste à rendre est > a la valeur de la pièce
                # (on suppose les pièces ordonnées par valeurs décroissantes)
                pieces.append(euroLib[i])
                searching = False
                aRendre -= euroTab[i]
            i += 1
        troubleshout += 1
        if troubleshout == 100000:
            raise TimeoutError('nombre de recherche trop important')

    return pieces

if __name__ == "__main__":
    listCounter(glouton(1))