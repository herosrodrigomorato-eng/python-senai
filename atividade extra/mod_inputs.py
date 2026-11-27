def receber_nome():
        nome=input("coloque seu nome :")
        return nome

def receber_idade():
    while True:
        try:
            idade=int(input("coloqeu ua idade : "))
            break
        except:
            print("coloque sua idade em anos !") 
    return idade

def receber_peso():
    while True:
        try:
            peso=float(input("coloque seu peso :"). replace(",","."))
            return peso
        except:
                print("coloque seu peso em caracteres vaidos !")





def soma(num1,num2):
   
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


def sub(num1,num2):
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

def mult(num1,num2):
      
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

def divisao(num1,num2):
        
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