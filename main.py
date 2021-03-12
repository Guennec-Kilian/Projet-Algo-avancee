euroLib = ["c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8"]
euroTab = [200, 100, 50, 20, 10, 5, 2, 1]


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
    return pieces


if __name__ == "__main__":
    print(glouton(138))