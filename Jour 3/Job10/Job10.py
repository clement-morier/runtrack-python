def pair(num):
    assert num > 0
    assert int(num)==num
    if num%2==0:
        print(f"{num} est un nombre pair")
    else:
        print(f"{num} est un nombre impair")        

pair(10)
pair(11)
pair(-10)