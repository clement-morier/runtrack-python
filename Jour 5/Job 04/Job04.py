def tapis(num):
    for i in range (1):
        print('+',end='');print((num-1)*'-',end='');print('+')
        for j in range(num-1):
            print('|',end='');print((num-2-j)*'#',end='');print(' ',end='');print(j*'#',end='');print('|')
    print('+',end='');print((num-1)*'-',end='');print('+') 

tapis(10)