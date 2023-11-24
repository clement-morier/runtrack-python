def parcour(marches,taille):
    c=0
    for t in range(5):
        for i in range (7):
            for j in range(2):
                for k in range(marches):
                    c+=taille
    c=c/100
    print(f"Pour {marches} marches de {taille} cm, le gardien parcourt {c} m par semaine")