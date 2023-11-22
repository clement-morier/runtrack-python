def calcul(num1,operator,num2):
    if operator=='*':
        print(num1*num2)
    elif operator=='-':
        print(num1-num2)
    elif operator=='+':
        print(num1+num2)
    elif operator=='/':
        print(num1/num2)
    elif operator=='%': 
        print(num1%num2)

calcul(15,'*',69)
calcul(50,'%',100)
calcul(16,'-',80)