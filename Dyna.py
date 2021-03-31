import constantes
euroLib = constantes.euroLib
euroTab = constantes.euroTab

print(euroLib)
print(euroTab)

#c'est l'algo glouton c'est pas dynamique dutout
def dynamique1(euroLib, euroTab, v):
    res = []
    def dynamique1_(euroTab, v, res,i):
        
        nb_piece = 0
        while (euroTab[i] * nb_piece <= v-euroTab[i]):
            nb_piece += 1
            
        
        res.append(nb_piece)
        print("valeur nb_piece ajouté =", nb_piece, " pour value =",
              euroTab[i], "x", nb_piece, "=", euroTab[i]*nb_piece)
        print("valeur de res est =",res)


        v -= euroTab[i]*nb_piece
        i += 1

        if (i < len(euroTab)):
            dynamique1_(euroTab, v, res, i)
        else:
            print("res vaut =", res)
            return res
    
    dynamique1_(euroTab, v,res, 0)

dynamique1(euroLib,euroTab, 489897)

