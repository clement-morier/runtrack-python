def bornes():
    L=[8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
    max=L[0]
    min=L[0]
    for i in range(len(L)-1):
        if L[i+1]>max:
            max=L[i+1]
    for i in range(len(L)-1):
        if L[i+1]<min:
            min=L[i+1]
    print(f"la valeur max est : {max}")
    print(f"la valeur min est : {min}")

bornes()