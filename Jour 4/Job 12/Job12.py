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

O=[8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
tri(O)