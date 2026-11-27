# estrutura case 
try: 
    num1= float(input("digite um numero   : ").replace( ",","."))
except: 
    print("operacao invalida! ")
 
try: 
    num2=float(input("digite o o segundo  número : ").replace(",","."))
except:
    print("valor invalido para o segundo numero!")

try:
    print("digite umas operações a seguir: \n")
    print("para multiplicações digite *")
    print("para adicao digite +")
    print("para subtracao - ")

    operador=str(input( " digite um operador "))
except: 
    print("operador invalido ")

match operador: 
    case "*" :
        resultado =num1 * num2 
        print(  num1,operador, num2 ," é = " , resultado )
    case "/":
        resultado= num1 / num2
        print( num1, operador, num2, " é = ", resultado )
    case "+": 
        resultado= num1 + num2 
        print( num1,operador, num2,"é = ", resultado )
    case "-":
        resultado= num1- num2
        print( num1, operador, num2, "é = ", resultado )
 