def Cesar(decalage,message):
    acrypter=message.upper()
    c=len(acrypter)
    messagecrypte=""
    for i in range(c):
        if acrypter[i]==' ':
            messagecrypte+=' '
        else:
            b=ord(acrypter[i])+decalage
            messagecrypte+=chr(b+26*((b<65)-(b>90)))
    print(messagecrypte)