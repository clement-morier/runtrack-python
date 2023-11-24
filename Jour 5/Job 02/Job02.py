def draw_rectangle(num1,num2):
    if num2%2==0:
        for i in range (num2):
            print('|', end='');print(num1*'-', end='');print('|')
    else :
        repete=int((num2)/2)
        for j in range(repete):
            print('|',end='');print(num1*'-',end='');print('|')
            print('|',end='');print(num1*' ',end='');print('|')
            print('|',end='');print(num1*'-',end='');print('|')