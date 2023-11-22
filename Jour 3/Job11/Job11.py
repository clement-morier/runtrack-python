def time_to_text(num):
    c=0
    heure=0
    while num > 60:
        num-=60
        c+=1
    print(f"{c} heures et {num} minutes")

time_to_text(500)