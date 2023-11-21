a=input('Entrer une longueur (a) :')
b=input('Entrer une longueur (b) :')
c=input('Entrer une longueur (c) :')
a=int(a)
b=int(b)
c=int(c)

if a >= b and a >= c:
    if a <= (b+c):
        if a**2==b**2+c**2:
            if a==b or a==c or b==c :
                print('Ce triangle est un triangle isocèle et rectangle')
            else:
                print('Ce triangle est un triangle rectangle')
        elif a==b and a==c :
            print('Ce triangle est un triangle equilatéral')
        elif a==b or a==b or b==c:
            print('Ce triangle est un triangle isocèle')
        else:
            print('Ce triange est un triangle quelconque')
    else :
        print ("Le triangle n'est pas constructible")
elif b >= a and b >= c:
    if b <= (a+c):
        if b**2==a**2+c**2:
            if a==b or a==c or b==c :
                print('Ce triangle est un triangle isocèle et rectangle')
            else:
                print('Ce triangle est un triangle rectangle')
        elif a==b and a==c :
            print('Ce triangle est un triangle equilatéral')
        elif a==b or a==b or b==c:
            print('Ce triangle est un triangle isocèle')
        else:
            print('Ce triange est un triangle quelconque')
    else :
        print ("Le triangle n'est pas constructible")
else:
    if c <= (a+b):
        if c**2==b**2+a**2:
            if a==b or a==c or b==c :
                print('Ce triangle est un triangle isocèle et rectangle')
            else:
                print('Ce triangle est un triangle rectangle')
        elif a==b and a==c :
            print('Ce triangle est un triangle equilatéral')
        elif a==b or a==b or b==c:
            print('Ce triangle est un triangle isocèle')
        else:
            print('Ce triange est un triangle quelconque')
    else :
        print ("Le triangle n'est pas constructible")