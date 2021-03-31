import Arbre
import constantes
import time
import matplotlib.pyplot as plt

A = Arbre.Arbre
euroLib = constantes.euroLib
euroTab = constantes.euroTab

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



def essaiSucc(a, N, solution=[]):
    # a le noeud que l'on traite
    # N la valeur a atteindre

    for k in range (len(euroLib)):
        if(a.valeur + euroTab[k] <= N):
            a.addFeuille(k) # ajout des différentes pièces utilisables et sommation avec la somme precedente

    i = 0
    solFound = False
    while i<len(a.feuilles) and not solFound:
        
        # on test ensuite les nouvelles sommes pour savoir si on a réussite
        if a.feuilles[i].isEqual(N):
            # si on a réussite et qu'elle est meilleurs que la précédente, on change la solution
            if len(solution) == 0 or len(solution) > a.feuilles[i].getLenChemin():
                solution = a.feuilles[i].getSortedChemin()
                solFound = True
        # sinon si on a une somme de valeur inferieur a ce qui doit etre rendu 
        #   ET 
        #       qu'aucune solution n'a été trouvée 
        #           OU 
        #       que le nombre de pièces nécessaires est inférieur au nombre de pièce de la solution
        elif a.feuilles[i].isLower(N) and (len(solution) == 0 or a.feuilles[i].getLenChemin() < len(solution)):
            # test la couche suivante de sommes dans l'arbre
            solution = essaiSucc(a.feuilles[i], N, solution)
        i+=1
    return solution

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
    t = time.time()
    sol = essaiSucc(A(0, [], -1), 1000)
    print(time.time() - t)