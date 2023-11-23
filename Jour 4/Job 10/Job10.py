def produits():
    L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
    c=0
    i=0
    while c==0 :
        if L[i]>25 and L[i]<90:
            c+=L[i]
        else:
            i+=1
        i+=1
    for j in range(len(L)-i):
        if L[j+i]>25 and L[j+i]<90:
            c=c*L[j+i]
    return (c)

print(produits())