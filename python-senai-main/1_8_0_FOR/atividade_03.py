#estrutura for 
resultado = 0
for adicao in range (1,6):
        inicio = True
        while inicio: 
            try: 
                numero = int(input("digite um numero inteiro :  "))
                print("numero",adicao,"=", numero )
                adicao +=1
                resultado = numero + resultado 
                inicio = False
            except ValueError: 
                print("coloque um numero valido ")
print("o resultado da some é ", resultado )