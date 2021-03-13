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
    

        

def glouton(aRendre):
    pieces =  []
    while aRendre != 0:
        searching = True
        i = 0
        while searching and i < len(euroLib):
            if aRendre >= euroTab[i]:
                pieces.append(euroLib[i])
                searching = False
                aRendre -= euroTab[i]
            i += 1
    print(pieces)
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
    X = []
    #euroLib = ["c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8"]
    #euroTab = [200, 100, 50, 20, 10, 5, 2, 1]
    def essaisSUCC(i,X,somcour):
        
        xi = 0
        X.append(0)
        print("valeur courante de X =",X)
        print("valeur de xi =",xi)
        print("valeur de W[i] =",W[i])
        print("valeur de somcour =",somcour)
        
        while (xi*W[i]<=M) : #Si ce produit est plus grand que M alors il est impossible de trouver une solution
            if((somcour + xi*W[i])<=M and (somcour+(xi+1))*W[i]>M):
                X[i]=xi
                somcour += xi*W[i]
                print("valeur de i =",i)
                print("valeur de lenW =",len(W))
                if(i+1<len(W)):
                    essaisSUCC(i+1,X,somcour)
                else:
                    return X
            xi+=1
    for k in range (len(X)-1):
        print("la pièce {0} apparait {1} fois".format(euroLib[k],X[k]))
    return essaisSUCC(0,X,somcour)

#algo ne liste pas toutes les solution parceque la condition du premier if est trop forte,
#la quantité de calcul est cependant vite astronomique sans (et en plus X deviendrait un tableau
#de tableaus pour stocker toutes les solutions :l
            






if __name__ == "__main__":
    listCounter(glouton(458))
    essaisSUCC_exe(458)