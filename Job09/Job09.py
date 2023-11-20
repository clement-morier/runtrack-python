nom='bonbon'
prix=1
quantité=100
print(nom)
print(prix)
print(quantité)
achat=input('Veuillez saisir la quantité de produits que vous souhaitez acheté :')
achat=int(achat)
quantité=int(quantité)
quantité=quantité-achat
prix=prix*1.1
print(nom)
print(prix)
print(quantité)