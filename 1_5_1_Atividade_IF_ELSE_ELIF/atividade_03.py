# estrutura if e else
try:
    valor = float(input("coloque o valor da compra:"))
    if valor < 0:
        print("valor invalido")
    else:
        if valor < 100:
                 print("sem desconto")
        elif valor >=100 and valor < 500:
                print("desconto de 10%")
        else: 
            if valor >=500:
                 print("desconto de 15%")
except:
    print("coloque apenas números")