import math

def soma():
    while True:
            try:
                num1=float(input("coloque o primeiro numero : "). replace(",","."))
                break
            except:
                print("coloque um numero !")
    while True:
                try:
                    num2=float(input("coloque o segundo  numero : "). replace(",","."))
                    break
                except: 
                    print("coloque apenas numeros!")
    soma = num1 + num2            

    print("o resultado é =", soma)


def sub():
    while True:
            try:
                num1=float(input("coloque o primeiro numero : "). replace(",","."))
                break
            except:
                print("coloque um numero !")
    while True:
                try:
                    num2=float(input("coloque o segundo  numero : "). replace(",","."))
                    break
                except: 
                    print("coloque apenas numeros!")
    subtracao = num1 - num2

    print("seu resultado é =",subtracao)

def mult():
      
    while True:
            try:
                num1=float(input("coloque o primeiro numero : "). replace(",","."))
                break
            except:
                print("coloque um numero !")
    while True:
                try:
                    num2=float(input("coloque o segundo  numero : "). replace(",","."))
                    break
                except: 
                    print("coloque apenas numeros!")
    multiplicacao= num1 * num2
    print("seu resultado é = ",multiplicacao)

def divisao():
        
    while True:
            try:
                num1=float(input("coloque o primeiro numero : "). replace(",","."))
                break
            except:
                print("coloque um numero !")
    while True:
                try:
                    num2=float(input("coloque o segundo  numero : "). replace(",","."))
                    break
                except: 
                    print("coloque apenas numeros!")
    divisao= num1 / num2
    print("seu resultado é = ",divisao)

#def calc():
print("===== CALCULADORA =====")
print("0 - sair()")
print("1 - Adição (+)")
print("2 - Subtração (-)")
print("3 - Multiplicação (*)")
print("4 - Divisão (/)")



while True:
    opcao = input("\nEscolha uma operação: ")

    if opcao == "0":
        print("Calculadora encerrada!")
        break
    if opcao  in ["1", "2", "3", "4"]:
            if opcao =="1":
                soma()
            elif opcao =="2":
                sub()
            elif opcao =="3":
                mult()
            elif opcao =="4":
                divisao()
          


