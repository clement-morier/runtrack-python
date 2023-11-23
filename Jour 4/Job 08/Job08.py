def somme_pair():
    L=[8, 24, 27, 48, 2,16, 9, 7, 84, 91]
    c=0
    for i in range(len(L)):
        if L[i]%2==0:
            c+=L[i]
    return(c)

print(somme_pair())