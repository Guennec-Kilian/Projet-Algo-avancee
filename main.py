import random
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

import math
if __name__ == "__main__":

    TempsCalcGlob = []
    nb_test = 20
    Nb_Valeurs = 500
    Val_Max = 1000000

    Vals = []
    for k in range(Nb_Valeurs):
        bornem = math.floor((Val_Max/Nb_Valeurs))
        Vals.append(random.randint(k*bornem,(k+1)*bornem))
    print("Valeurs Test=", Vals)
    
    for k in range (nb_test) :
        
        TempsCalc = [[],[],[]]
        
        for testvalue in Vals :

            t = time.time()
            print(glouton(testvalue))
            TempsCalc[0].append(time.time()-t)
            t = time.time()
            #sol = essaiSucc(A(0, [], -1), testvalue)
            TempsCalc[1].append(time.time()-t)
            #print(sol)
            t = time.time()
            print(dynamique(testvalue))
            TempsCalc[2].append(time.time()-t)
            t = time.time()
        
        TempsCalcGlob.append(TempsCalc)

    TempsMoyens = [[0]*len(Vals),[0]*len(Vals),[0]*len(Vals)]
    EcartType = [[0]*len(Vals), [0]*len(Vals), [0]*len(Vals)]
    
    for k in range(len(TempsCalcGlob)):
        #Parcours des tests pour une liste aléatoire de quantité de monnaie à rendre donnée
        for i in range(len(TempsCalcGlob[k])):
            #Parcours des résultat de tests séparément
            for p in range(len(TempsCalcGlob[k][i])):
                #parcours du résultats d'un test en particulier pour une valeur à rendre en particulier, unitaire
                TempsMoyens[i][p]+=TempsCalcGlob[k][i][p]

    #print("TempsMoyens pre moyennage=",TempsMoyens)

    for k in range(len(TempsMoyens)):
        for i in range(len(TempsMoyens[0])):
            TempsMoyens[k][i] = TempsMoyens[k][i]/nb_test

    #print("TempsMoyens final =",TempsMoyens)

    for k in range(len(TempsCalcGlob)):
        #Parcours des tests pour une liste aléatoire de quantité de monnaie à rendre donnée
        for i in range(len(TempsCalcGlob[k])):
            #Parcours des résultat de tests séparément
            for p in range(len(TempsCalcGlob[k][i])):
                #parcours du résultats d'un test en particulier pour une valeur à rendre en particulier, unitaire
                EcartType[i][p] = abs(TempsMoyens[i][p] - TempsCalcGlob[k][i][p])
            
    for k in range(len(TempsMoyens)):
        for i in range(len(TempsMoyens[0])):
            EcartType[k][i] = (EcartType[k][i]/nb_test)
    
    print("ecart type par valeur = ",EcartType)
    print("Valeurs Test=", Vals)

    
    fig, axs = plt.subplots(2)
    fig.suptitle('Resultats test/temps || Resultats ecart-type/temps')
    for k in range(len(TempsMoyens)):
        axs[0].plot(Vals, TempsMoyens[k])
    for k in range(len(TempsMoyens)):
        axs[1].plot(Vals, EcartType[k])

    fig.savefig("mygraph.png")
