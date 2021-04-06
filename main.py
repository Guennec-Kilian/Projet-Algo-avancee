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
    #varList[1] contient le nombre de fois que chaque piece apparait
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


def dynamique(aRendre):

    pieces = [0]*len(euroTab)
    res = []

    pieces[-1] = aRendre//euroTab[-1]

    l = 2
    while l <= len(euroTab):
        pieces[-l] = (pieces[-l+1]*euroTab[-l+1])//euroTab[-l]
        pieces[-l+1] -= (pieces[-l]*euroTab[-l])//euroTab[-l+1]
        aRendreTemp = 0
        for i in range(len(euroTab)-l, len(euroTab)):
            aRendreTemp += (pieces[i]*euroTab[i])
        aRendreTemp -= aRendre
        if aRendreTemp < 0:
            aRendreTemp *= -1
            for i in range(len(euroTab)-l+1, len(euroTab)):
                temp = aRendreTemp//euroTab[i]
                aRendreTemp -= temp*euroTab[i]
                pieces[i] += temp
        elif aRendreTemp > 0:
            for i in range(len(euroTab)-l+1, len(euroTab)):
                temp = aRendreTemp//euroTab[i]
                aRendreTemp -= temp*euroTab[i]
                pieces[i] -= temp

        l += 1
    
    for i in range(len(euroLib)):
        res += [euroLib[i]]*pieces[i]

    return res

def glouton(aRendre):
    pieces =  []
    res = []
    troubleshout = 0
    for i in range(len(euroTab)):
        pieces.append(aRendre // euroTab[i])
        aRendre -= (pieces[i] * euroTab[i])
        res += [euroLib[i]] * pieces[i] 

    return res

if __name__ == "__main__":
    #print(glouton(191))
    #t = time.time()
    sol = essaiSucc(A(0, [], -1), 191)
    #print(time.time() - t)
    print(sol)
    print(dynamique(191))