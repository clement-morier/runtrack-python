def inverser(mot):
    if len(mot) == 0:
        print(mot)
    else:
        c=len(mot)
        print(mot[c::-1])

inverser('nikana')