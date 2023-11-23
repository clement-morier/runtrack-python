def echange(L):
    c=L[-1]
    L[-1]=L[0]
    L[0]=c
    return L

I=[1,2,3,4,5]
print(echange(I))