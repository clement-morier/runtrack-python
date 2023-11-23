def my_long_word(num,chaine):
    c=0
    i=0
    h=0
    o=0
    r=1
    newchaine=''
    L=[]
    vide=[]
    vide2=[]
    mot=''
    mot1=''
    mot2=''
    for elem in chaine :
        i+=1
        c+=1
        if elem ==' ':
            for j in range(c-1):
                if chaine[i-c+j]!= ',':
                    mot=mot+chaine[i-c+j]
            vide=[mot]
            mot=''
            L=L+vide
            c=0
    while chaine[-r] != ' ':
        r+=1
    if r>3 :
        for z in range(r-1):
            mot1=mot1+chaine[i+1-r+z]
        vide=[mot1]
        L=L+vide
    for elem1 in L:
        h+=1
    for k in range(h):
        mot2=(L[k])
        for elem in mot2:
            o+=1
        if o>num:
            newchaine=newchaine+' '+L[k]
        o=0
    print(newchaine)

my_long_word(3,'La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance')