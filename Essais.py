euroLib = ["c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8"]
euroTab = [200, 100, 50, 20, 10, 5, 2, 1]

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

#Analyse
#W = vecteur contenant les valeurs de chaque piece.
#Domaine de solution de la valeur "nombre de fois qu'une piece est utilisée" :
#xi dans |[0;+inf|[ , par inf on entend partie entière valeur demandée/valeur de la piece, valeur demandée non bornée
#vecteur Si : vecteur de valeurs xi
#solution : tableau X[1:n] avec n le nombre de pieces disponibles
#Une solution est représentée par n vecteur X tel que Somme(W[k]*X[k]) = valeur demandée (M)
#Pour tout i, X[i] est le nombre de piece d'index i présentent dans la solution

#satisfaisant(xi)
#somcour + xi * W[i] <= M

#enregistrer
#X[i] <- xi ; somcour <- somcour + xi*W[i]

#soltrouvée
#somcour = M

#défaire
#somcour <- somcour - xi*W[i]

#encorepossible
#i<n

#une condition d'élaguage est de ne pas pouvoir former une somme somcour inférieure à M
#avec les valeurs de W restantes

def essaisSUCC_exe(M):
    somcour = 0
    rk = 0
    W = euroTab
    X = [0,0,0,0,0,0,0,0]
    #euroLib = ["c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8"]
    #euroTab = [200, 100, 50, 20, 10, 5, 2, 1]
    def essaisSUCC(i,X,somcour):
        
        xi = 0
        
        while (xi*W[i]<=M) : #Si ce produit est plus grand que M alors il est impossible de trouver une solution
            if((somcour + xi*W[i])<=M and (somcour+(xi+1))*W[i]>M):
                X[i]=xi
                somcour += xi*W[i]
                print("valeur de xi =",xi)
                if(i+1<len(W) and somcour!=M):
                    essaisSUCC(i+1,X,somcour)
                else:
                    for k in range (len(X)):
                        print("la pièce {0} apparait {1} fois".format(euroLib[k],X[k]))
                    return X

            
            print("valeur de xi =",xi, "valeur de i=",i)
            xi+=1

        


    return essaisSUCC(0,X,somcour)

#algo ne liste pas toutes les solution parceque la condition du premier if est trop forte,
#la quantité de calcul est cependant vite astronomique sans (et en plus X deviendrait un tableau
#de tableaus pour stocker toutes les solutions :l
            

#Cette fois la fonction renvoie toutes les possibilités possibles
def essaissuccessifs_exe(M):
    somcour = 0
    rk = 0
    W = euroTab
    X = [0,0,0,0,0,0,0,0]
    XList = [] 
    #euroLib = ["c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8"]
    #euroTab = [200, 100, 50, 20, 10, 5, 2, 1]
    def essaissuccessifs(i,X,somcour):

        #Verification que l'on ne soit pas arrivé au bout de W avant de continuer, si c'est le cas, alors on a X
        if(i>=len(W)):
            return X
        
        xi = 1
        rk = M-somcour
        
        while (xi*W[i]<=M) : #Si ce produit est plus grand que M alors il est impossible de trouver une solution
            #Conditions d'élagage 1: On s'arrette de cherche quand la plus petite piece est supérieur à M-somcour (donc jamais atteinte quand le nb de piece de 1ct est illimité)
            #Conditions d'élagage 2: On s'arrete de chercher quand somcour = M

            #Calcul de la valeur potentielle xi*W[i] quee l'on ajouterait dans un X
            pot = xi*W[i]

            #On vérifie que cette valeur ajoutée à somcour ne dépasse pas M
            if(somcour+pot<=M) :
                #On veut maintenant passer aux étapes suivantes :
                #Une direction qui conserve ce coef xi pour l'indice i, et étudie i+1, et une autre qui regarde le xi+1

                #On peut ajouter ce coef de piece d'index i au X courant
                Y = X
                Y[i]=xi



                #Départ dans la première direction avec somcour mise à jour, on vérifie que l'on n'ait pas atteind la fin de la liste
                if(i+2<=len(W) and (somcour+pot)!=M):
                    
                    essaissuccessifs(i+1,X,somcour+pot)
                    
                else:
                    #Si on a atteint la fin de W ou alors que l'on a une solution (cond 2), on renvoie X
                    return X
                #Départ dans la deuxième direction avec somcour non mise à jour

            
            xi+=1

            

        


    return essaisSUCC(0,X,somcour)




if __name__ == "__main__":

    listCounter(glouton(4000))
    essaisSUCC_exe(400)