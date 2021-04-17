import constantes
import copy
import random
import Arbre
import constantes
import time
import math
import copy
import matplotlib.pyplot as plt
euroLib = constantes.euroLib
euroTab = constantes.euroTab
nmax = -1
XList = []
nbr = 0

def essaissuccessifsOPT_exe2(M):
    global nbr 
    nbr = 0
    sumc = 0
    X = [0, 0, 0, 0, 0, 0, 0, 0]
    n = 0
    #n défini le nombre de pièces utilisées pour arriver à la somme finale

    def essaissuccessifsOPT(i, X, sumc, n):
        
        global nmax
        #print("entering function with values i =",i,', X=',X,", sumc = ",sumc,", n =",n,", nmax =",nmax)
        global nbr

        #parcours de la liste euroTab par index :
        if(sumc<M and i>0):
            #print("parcours en INDEX")
            essaissuccessifsOPT(i-1,X,sumc,n)
            nbr+=1
        else:
            #soit nous sommes arrivés à la valeur recherchée
            #soit nous sommes arrivés au bout de la liste euroTab
            #soit aucun des deux cas précédents : on peut continuer à incrémenter le nombre de piece d'indice i
            #il faut respectivement =1= mettre à jour nmax
            if (sumc == M and (nmax > n or nmax == -1)):
                nmax = n
                #print("mise à jour de nmax avec nmax=",nmax)
                #print("===================================== resultat trouvé : X=", X)
                global XList
                XList.append(X)
            #else:
                #print("reached end of INDEX tree with i=",i,', X=',X,", sumc = ",sumc,", n =",n,", nmax =",nmax,"->")
                
        #=2= incrémenter le nombre de piece

        #print("reaching VALUE PRE incrementation part i =",i,', X=',X,", sumc = ",sumc,", n =",n,", nmax =",nmax)
        Y=copy.deepcopy(X)
        Y[i]+=1
        sumc+=euroTab[i]
        n+=1
        #print("reaching VALUE POST incrementation part i =",i,', X=',Y,", sumc = ",sumc,", n =",n,", nmax =",nmax)
        #avant de d'appeler récursivement la fonction, on vérifie les deux conditions suivantes
        if(sumc<M and (nmax>n or nmax==-1)):
            #print("parcours en VALUE")
            essaissuccessifsOPT(i,Y,sumc,n)
            nbr+=1
        else:
            #soit nous sommes arrivés à la valeur recherchée
            #soit nous sommes arrivés à n = nmax
            #soit les deux cas précédents sont réalisés : on peut ajouter X à la liste des solutions
            if (sumc == M and (nmax > n or nmax == -1)):
                nmax = n
                #print("mise à jour de nmax avec nmax=",nmax)
                #print("!!!!!!!!!!!!!!!!!!! resultat trouvé : X=",Y)
                XList.append(Y)
            #else :
                #print("reached end of VALUE tree with i=",i,', X=',Y,", sumc = ",sumc,", n =",n,", nmax =",nmax,"++")
                

    essaissuccessifsOPT(len(euroTab)-1, X, sumc, n)
    global XList
    print("XLIST =",XList)
    print(nbr)
    
    nmax = -1
    XList = []
    return nbr
    
def essaissuccessifsSansElagage(M):
    global nbr 
    nbr = 0
    sumc = 0
    X = [0, 0, 0, 0, 0, 0, 0, 0]
    n = 0
    #n défini le nombre de pièces utilisées pour arriver à la somme finale

    def essaissuccessifsOPT(i, X, sumc, n):

        global nmax
        #print("entering function with values i =",i,', X=',X,", sumc = ",sumc,", n =",n,", nmax =",nmax)
        global nbr

        #parcours de la liste euroTab par index :
        if(sumc < M and i > 0):
            #print("parcours en INDEX")
            essaissuccessifsOPT(i-1, X, sumc, n)
            nbr+=1
        else:
            #soit nous sommes arrivés à la valeur recherchée
            #soit nous sommes arrivés au bout de la liste euroTab
            #soit aucun des deux cas précédents : on peut continuer à incrémenter le nombre de piece d'indice i
            #il faut respectivement =1= mettre à jour nmax
            if (sumc == M):
                nmax = n
                #print("mise à jour de nmax avec nmax=",nmax)
                #print("===================================== resultat trouvé : X=", X)
                global XList
                XList.append(X)
            #else:
                #print("reached end of INDEX tree with i=",i,', X=',X,", sumc = ",sumc,", n =",n,", nmax =",nmax,"->")

        #=2= incrémenter le nombre de piece

        #print("reaching VALUE PRE incrementation part i =",i,', X=',X,", sumc = ",sumc,", n =",n,", nmax =",nmax)
        Y = copy.deepcopy(X)
        Y[i] += 1
        sumc += euroTab[i]
        n += 1
        #print("reaching VALUE POST incrementation part i =",i,', X=',Y,", sumc = ",sumc,", n =",n,", nmax =",nmax)
        #avant de d'appeler récursivement la fonction, on vérifie les deux conditions suivantes
        if(sumc < M):
            #print("parcours en VALUE")
            essaissuccessifsOPT(i, Y, sumc, n)
            nbr+=1
        else:
            #soit nous sommes arrivés à la valeur recherchée
            #soit nous sommes arrivés à n = nmax
            #soit les deux cas précédents sont réalisés : on peut ajouter X à la liste des solutions
            if (sumc == M):
                nmax = n
                #print("mise à jour de nmax avec nmax=",nmax)
                #print("!!!!!!!!!!!!!!!!!!! resultat trouvé : X=",Y)
                XList.append(Y)
            #else :
                #print("reached end of VALUE tree with i=",i,', X=',Y,", sumc = ",sumc,", n =",n,", nmax =",nmax,"++")

    essaissuccessifsOPT(len(euroTab)-1, X, sumc, n)
    global XList
    global nmax
    nmax = -1
    XListRes = copy.deepcopy(XList)
    print("XLIST =",XList)
    XList = []
    
    print(nbr)
    return nbr


val = 7
essaissuccessifsOPT_exe2(val)
nbr = 0
essaissuccessifsSansElagage(val)

if __name__ == "__main__":

    k = 0
    TempsCalcGlob = []
    nb_test = 1 #Nombre de fois qu'un meme calcul sera effectué, pour palier au problemes des processus en arrière plan à impacte aléatoire sur les durées de calcul
    Nb_Valeurs = 20 #Nombres de valeurs testées, entre 0 et la valeur max choisie
    Val_Max = 100 #Valeur max choisie
    flatfact = 0.2  # taille de l'intervalle sur lequel on calcul la moyenne pour lissage, 1 = lissage sur l'ensemble de la courbe

    t_Int = int(max(math.floor(flatfact*Nb_Valeurs*0.5), 1))

    Vals = []
    for k in range(Nb_Valeurs):
        bornem = math.floor((Val_Max/Nb_Valeurs))
        Vals.append(random.randint(k*bornem,(k+1)*bornem))

    for k in range(int(t_Int)):
        Vals.append(Vals[-1])

    #Remplissage d'une liste TempsCalcGlobal avec le resultat de chacun des test réalisé, pour chaque algo, pour chaque valeur à rendre, pour toute les itérations
    
    for k in range (nb_test) :
        
        TempsCalc = [[],[]]
        
        for testvalue in Vals :

            t = time.time()
            #print(essaissuccessifsSansElagage(testvalue))
            TempsCalc[0].append(essaissuccessifsSansElagage(testvalue))
            t = time.time()
            #print(essaissuccessifsOPT_exe2(testvalue))
            TempsCalc[1].append(essaissuccessifsOPT_exe2(testvalue)*10)
        
        TempsCalcGlob.append(TempsCalc)

    TempsMoyens = [[0]*len(Vals),[0]*len(Vals)]
    EcartType = [[0]*len(Vals), [0]*len(Vals)]

    #Construction d'une liste de sommes de résultats de chaque itération (pour construire la moyenne ensuite)
    
    for k in range(len(TempsCalcGlob)):
        #Parcours des tests pour une liste aléatoire de quantité de monnaie à rendre donnée
        for i in range(len(TempsCalcGlob[k])):
            #Parcours des résultat de tests séparément
            for p in range(len(TempsCalcGlob[k][i])):
                #parcours du résultats d'un test en particulier pour une valeur à rendre en particulier, unitaire
                TempsMoyens[i][p]+=TempsCalcGlob[k][i][p]

    #print("TempsMoyens pre moyennage=",TempsMoyens)

    #Construction de la moyenne

    for k in range(len(TempsMoyens)):
        for i in range(len(TempsMoyens[0])):
            TempsMoyens[k][i] = TempsMoyens[k][i]/nb_test

    print("TempsMoyens final =",TempsMoyens)

    #Construction de la liste des écart type

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

    #Lissage des résultats obtenus pour une meilleure présentation

    TempsMoyensLissage = [[0]*len(Vals), [0]*len(Vals)]
    TempsMoyensLissageSliced = []

    for k_test in range(len(TempsMoyens)):

        for k_v_temps in range(len(TempsMoyens[k_test])):

            #print("k_v_temps =",k_v_temps)

            Int_Local = [TempsMoyens[k_test][k_v_temps]]
            tmp = k_v_temps-1
            while(tmp>=0 and tmp >= k_v_temps-t_Int):
                Int_Local.insert(0, TempsMoyens[k_test][tmp])
                #print("tmp dans boucle neg =", tmp)
                tmp-=1
                
            tmp = k_v_temps+1

            while(tmp < len(TempsMoyens[0]) and tmp <= k_v_temps+t_Int):
                Int_Local.append(TempsMoyens[k_test][tmp])
                #print("tmp dans boucle pos =", tmp)
                tmp+=1

            moy = sum(Int_Local)/t_Int

            TempsMoyensLissage[k_test][k_v_temps] = moy

        s = slice(0, len(Vals)-t_Int)
        TempsMoyensLissageSliced.append(TempsMoyensLissage[k_test][s])

    s2 = slice(0, len(Vals)-t_Int)
    ValsSliced = copy.deepcopy(Vals[s])

    print("lissage =",TempsMoyensLissage)
    print("lissageSlice =", TempsMoyensLissageSliced)

    print("t_Int =", t_Int)
    print("Valeurs Test=", Vals)
    print("ValsSliced =", ValsSliced)

    fig, axs = plt.subplots(1)
    fig.suptitle('Resultats test/temps || Resultats ecart-type/temps')
    for k in range(len(TempsMoyens)):
        axs.plot(Vals, TempsMoyens[k])
    #filename = "graph&nb_test="+str(nb_test)+"&Nb_Valeurs="+str(Nb_Valeurs)+"&ValMax="+str(Val_Max)+"&flatfact="+str(flatfact)+".png"
    filename = "NombreAppelsRecusrifsComparaison.png"
    fig.savefig(filename)