euroLib = ["c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8"]
euroTab = [2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]


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
        


if __name__ == "__main__":
    print(glouton(12.38))