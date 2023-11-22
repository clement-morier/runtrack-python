def moyenne(num1,num2,num3):
    return((num1+num2+num3)/3)

moyenne1=input('Entrez la 1er moyenne')
moyenne2=input('Entrez la 2eme moyenne')
moyenne3=input('Entrez la 3eme moyenne')
moyenne1=int(moyenne1)
moyenne2=int(moyenne2)
moyenne3=int(moyenne3)
moyenne_etudiant=moyenne(moyenne1,moyenne2,moyenne3)
if moyenne_etudiant >= 15 :
    print('Très bon élève')
elif moyenne_etudiant >= 11 :
    print('Bon élève')
elif moyenne_etudiant >= 8 :
    print('Elève moyen')
else :
    print('Elève devant faire des efforts')

