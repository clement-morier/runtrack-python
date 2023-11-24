def arrondit(L):
    L1=[]
    c=0
    for i in range(len(L)):
        if L[i]<=40:
            L1.append(L[i])
        else:
            if L[i]%5==0:
                L1.append(L[i])
            else:
                b=L[i]
                while L[i]%5!=0:
                    c+=1
                    L[i]=L[i]+1
                if c<3:
                    L1.append(b+c)
                else:
                    L1.append(b)
                c=0
    return(L1)

N=[26,48,45,50,56,84,81]
print(arrondit(N))