def doublons():
    c=0
    L=[10,20,30,20,10,50,60,40,80,50,40]
    L_unique=[]
    vide=[]
    for elem in L :
        if elem not in L_unique:
            vide=[elem]
            L_unique=L_unique+vide
    print(L_unique)

doublons()