# estrutura def
def soma(num1,num2):
    soma = num1 + num2 
    return soma 

start=True
while start:
    try: 
        num1 = float(input("digite o primeiro numero :").replace (".",","))
        start = False 
    except: 
        print(" valor invalido ! digite aenas numeros !")
start=True
while start:
    try: 
        num2= float(input("digite o segundo numero : ").replace(".",","))
        start= False
    except: 
        print(" valor invalido ! digite aenas numeros !")
resultado = soma(num1, num2)
print("o valor da soma é = ", resultado)