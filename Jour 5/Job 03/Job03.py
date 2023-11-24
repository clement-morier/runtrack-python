def triangle(num):
    for i in range (num-1):
            print((int(num)-i)*' ',end='');print('/',end='');print(i*2*' ',end='');print("\\")
    print(' ',end='');print('/',end='');print(((i*2)+2)*'-',end='');print('\\')

triangle(10)