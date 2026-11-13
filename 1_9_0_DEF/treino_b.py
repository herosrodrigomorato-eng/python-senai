#estrutura def 
def calcular_media(num1, num2,  num3 ):
    calcular_media= ((num1 +num2+ num3) /3)
    return calcular_media

def receber_mensagem(mensagem):
    start=True
    while start:
        try:
            numero=float(input(mensagem).replace(".",","))
            start=False
        except:
            print("valor inadequado ! coloque um valor valido!")
    return numero 
num1=receber_mensagem("coloque  o primeiro numero : ")
num2=receber_mensagem("coloque  o segundo numero : ")
num3=receber_mensagem("coloque  o terceiro  numero : ")

resultado = calcular_media(num1, num2, num3)
print("A media é =", resultado )