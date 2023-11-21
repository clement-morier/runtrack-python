h=input('Entrez un entier supérieur à zéro (N) :')
assert h!=0
h=int(h)
for i in range (h):
    print(f'Table de multiplication de {i+1}:')
    for j in range (10):
        print(f"{i+1}x{j+1}={(i+1)*(j+1)}")