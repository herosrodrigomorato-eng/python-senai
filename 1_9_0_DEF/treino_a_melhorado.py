# estrutura def
def soma(num1,num2):
    soma=num1+num2
    return soma   
start=True
def receber_mensagem(mensagem):
    try:
        numero=int(input(mensagem).replace(",","."))
        start=False
    except:
        print("valor incorreto  por favor digite apenas numeros")
    return numero
    
num1=receber_mensagem("digite o primeiro numero : ")
num2=receber_mensagem("digite o segundo  numero : ")

resultado= soma(num1, num2)
print("O valor da soma é =",resultado)