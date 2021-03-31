import constantes
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
                        nmax = n

                        sum = 0
                        for k in range(len(X)):
                            sum += X[k]

                        print("==========un i max a été atteint =", i, " X=",
                              X, " somc=", somcour, " p=", sum)

                        return XList.append(X)
                else:
                    nmax = n
                    sum = 0
                    for k in range(len(X)):
                        sum += X[k]

                    print("un i max a été atteint =============", i, " X=",
                          X, " somc=", somcour, " p=", sum)

                    return XList.append(X)

            else:
                print("X non satisfaisant")
                return -1

        xi = 0
        rk = M-somcour
        xi_flag = True

        # Si ce produit est plus grand que M alors il est impossible de trouver une solution
        while (xi * W[i] + somcour <= M and xi_flag):
            print("somcour =",somcour)
            #Condition d'élagage 1: On s'arrete de cherche quand la plus petite piece est supérieur à M-somcour (donc jamais atteinte quand le nb de piece de 1ct est illimité)
            #Condition d'élagage 2: On s'arrete de chercher quand somcour = M
            #Condition d'élagage 3: On s'arrete de chercher quand n est supérieur à nmax

            #Calcul de la valeur potentielle xi*W[i], on ajoutera xi dans un X
            pot = xi*W[i]
            #On veut maintenant passer aux étapes suivantes :
            #Une direction qui conserve ce coef xi pour l'indice i, et étudie i+1, et une autre qui regarde le xi+1

            #Départ dans la première direction avec somcour et X mises à jour, on ajoute +1 à n
            
            print("boucle avec : i =", i, "xi =", xi, " n=", n, "nmax =", nmax)

            #condition 3
            if(n <= nmax or nmax == -1):
                #On peut ajouter ce coef de piece d'index i au X courant et continuer à chercher
                Y = X
                Y[i] = xi
                print("boucle avec : i =", i, "xi =", xi, " X =", X,
                      " scour+pot=", somcour+pot, " n=", n, "nmax =", n)
                essaissuccessifsOPT(i+1, Y, somcour+pot, n+xi)

            else:
                #Il ne sert à rien de continuer à faire croitre xi, et on veut sortir de la boucle
                #On veut meme sortir de cette branche entièrement
                
                xi_flag = False

            #Départ dans la deuxième direction, une simple incrémentation du nombre de pieces d'indice i
            xi += 1
            n+=1

    return essaissuccessifsOPT(0, X, somcour, n)


essaissuccessifsOPT_exe(4)