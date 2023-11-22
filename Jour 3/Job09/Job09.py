def moyenne(num1,num2,num3):
    return((num1+num2+num3)/3)
moyenne1=float(input('Entrez la 1ere moyenne'))
while moyenne1>20:
    moyenne1=float(input('Entrer une moyenne sur 20'))
moyenne2=float(input('Entrez la 2eme moyenne'))
while moyenne2>20:
    moyenne2=float(input('Entrer une moyenne sur 20'))
moyenne3=float(input('Entrez la 3eme moyenne'))
while moyenne3>20:
    moyenne3=float(input('Entrer une moyenne sur 20'))
moyenne_etudiant=moyenne(moyenne1,moyenne2,moyenne3)
if moyenne_etudiant >= 15 :
    print('Très bon élève')
elif moyenne_etudiant >= 11 :
    print('Bon élève')
elif moyenne_etudiant >= 8 :
    print('Elève moyen')
else :
    print('Elève devant faire des efforts')