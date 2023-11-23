def tri(L):
    c=0
    for elem in L :
        c+=1
    for n in range(1,c):
        cle = L[n]
        j = n-1
        while j>=0 and L[j] > cle:
            L[j+1] = L[j] 
            j = j-1
        L[j+1] = cle
    print(L)

def arrondi():
    c=0
    L=[22.4, 4.0, 16.22, 9.10, 11.00,12.22, 14.20, 5.20, 17.50]
    for elem in L:
        c+=1
    for i in range(c):
        if L[i]-int(L[i])>=0.5:
            L[i]=int(L[i])+1
        else:
            L[i]=int(L[i])
    print(tri(L))

arrondi()