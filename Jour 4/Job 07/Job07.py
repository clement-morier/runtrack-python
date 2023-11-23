def multiple():
    L=[8,24,48,2,16]
    c=0
    for i in range(len(L)):
        if L[i]%3==0:
            c+=1
    return(c)

print(multiple())