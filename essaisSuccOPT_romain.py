import constantes
import copy
euroLib = constantes.euroLib
euroTab = constantes.euroTab

nmax = -1

def essaissuccessifsOPT_exe(M):

    somcour = 0
    rk = 0
    W = euroTab
    X = [0, 0, 0, 0, 0, 0, 0, 0]
    XList = []
    n = 0
    #n défini le nombre de pièces utilisées pour arriver à la somme finale

    def essaissuccessifsOPT(i, X, somcour, n):
        global nmax

        #Verification que l'on ne soit pas arrivé au bout de W avant de continuer, si c'est le cas, alors on a X
        if(i >= len(W)):
            if(somcour == M):
                # mise à jour de nmax
                if(nmax != -1):
                    if(n < nmax):
                        
                        sum = 0
                        for k in range(len(X)):
                            sum += X[k]

                        nmax = sum

                        print("==========un i max a été atteint =", i, " X=",
                              X, " somc=", somcour, " p=", sum,'nmax =', nmax)

                        return XList.append(X)
                else:
                    
                    sum = 0
                    for k in range(len(X)):
                        sum += X[k]
                    nmax = sum

                    print("un i max a été atteint =============", i, " X=",
                          X, " somc=", somcour, " p=", sum,'nmax =', nmax)

                    return XList.append(X)

            else:
                #print("X non satisfaisant")
                return -1

        else :
            xi = 0
            rk = M-somcour
            xi_flag = True
            # Si ce produit est plus grand que M alors il est impossible de trouver une solution
            while (xi * W[i] + somcour <= M and xi_flag):
                #print("somcour =",somcour)
                #Condition d'élagage 1: On s'arrete de cherche quand la plus petite piece est supérieur à M-somcour (donc jamais atteinte quand le nb de piece de 1ct est illimité)
                #Condition d'élagage 2: On s'arrete de chercher quand somcour = M
                #Condition d'élagage 3: On s'arrete de chercher quand n est supérieur à nmax

                #Calcul de la valeur potentielle xi*W[i], on ajoutera xi dans un X
                pot = xi*W[i]
                #On veut maintenant passer aux étapes suivantes :
                #Une direction qui conserve ce coef xi pour l'indice i, et étudie i+1, et une autre qui regarde le xi+1

                #Départ dans la première direction avec somcour et X mises à jour, on ajoute +1 à n
                
                #print("boucle avec : i =", i, "xi =", xi, " n=", n, "nmax =", nmax)

                #condition 3
                if(n <= nmax or nmax == -1):
                    #On peut ajouter ce coef de piece d'index i au X courant et continuer à chercher
                    Y = X
                    Y[i] = xi
                    #print("boucle avec : i =", i, "xi =", xi, " X =", X," scour+pot=", somcour+pot, " n=", n, "nmax =", n)
                    essaissuccessifsOPT(i+1, Y, somcour+pot, n+xi)

                else:
                    #Il ne sert à rien de continuer à faire croitre xi, et on veut sortir de la boucle
                    #On veut meme sortir de cette branche entièrement
                    
                    xi_flag = False

                #Départ dans la deuxième direction, une simple incrémentation du nombre de pieces d'indice i
                xi += 1
                n+=1

    return essaissuccessifsOPT(0, X, somcour, n)

nmax = -1
XList = []
#euroTabOpt = euroTab.reverse()
def essaissuccessifsOPT_exe2(M):

    sumc = 0
    X = [0, 0, 0, 0, 0, 0, 0, 0]
    n = 0
    #n défini le nombre de pièces utilisées pour arriver à la somme finale

    def essaissuccessifsOPT(i, X, sumc, n):
        
        global nmax
        print("entering function with values i =",i,', X=',X,", sumc = ",sumc,", n =",n,", nmax =",nmax)
        

        #parcours de la liste euroTab par index :
        if(sumc<M and i>0):
            print("parcours en INDEX")
            essaissuccessifsOPT(i-1,X,sumc,n)
        else:
            #soit nous sommes arrivés à la valeur recherchée
            #soit nous sommes arrivés au bout de la liste euroTab
            #soit aucun des deux cas précédents : on peut continuer à incrémenter le nombre de piece d'indice i
            #il faut respectivement =1= mettre à jour nmax
            if (sumc == M and (nmax > n or nmax == -1)):
                nmax = n
                print("mise à jour de nmax avec nmax=",nmax)
                print("===================================== resultat trouvé : X=", X)
                global XList
                XList.append(X)
            else:
                print("reached end of INDEX tree with i=",i,', X=',X,", sumc = ",sumc,", n =",n,", nmax =",nmax,"->")

        #=2= incrémenter le nombre de piece

        #print("reaching VALUE PRE incrementation part i =",i,', X=',X,", sumc = ",sumc,", n =",n,", nmax =",nmax)
        Y=copy.deepcopy(X)
        Y[i]+=1
        sumc+=euroTab[i]
        n+=1
        #print("reaching VALUE POST incrementation part i =",i,', X=',Y,", sumc = ",sumc,", n =",n,", nmax =",nmax)
        #avant de d'appeler récursivement la fonction, on vérifie les deux conditions suivantes
        if(sumc<M and (nmax>n or nmax==-1)):
            print("parcours en VALUE")
            essaissuccessifsOPT(i,Y,sumc,n)
        else:
            #soit nous sommes arrivés à la valeur recherchée
            #soit nous sommes arrivés à n = nmax
            #soit les deux cas précédents sont réalisés : on peut ajouter X à la liste des solutions
            if (sumc == M and (nmax > n or nmax == -1)):
                nmax = n
                print("mise à jour de nmax avec nmax=",nmax)
                print("!!!!!!!!!!!!!!!!!!! resultat trouvé : X=",Y)
                XList.append(Y)
            else :
                print("reached end of VALUE tree with i=",i,', X=',Y,", sumc = ",sumc,", n =",n,", nmax =",nmax,"++")

    essaissuccessifsOPT(len(euroTab)-1, X, sumc, n)
    print("XLIST =",XList)

    


essaissuccessifsOPT_exe2(9)
