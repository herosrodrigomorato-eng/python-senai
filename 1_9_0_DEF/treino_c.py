#estrutura def 
start=True
def calcular_desconto( preco , desconto ):
    preco_final= preco -(preco * (desconto/100))
    return  preco_final 

def recebe_numero(mensagem ):

    while True:
        try: 
            preco=float(input(mensagem).replace(",","."))
            break
        except ValueError: 
            print(" coloque um numero valido !")
    return preco 

preco = recebe_numero("coleque o preco: ")
desconto=recebe_numero("coloque o desconto: ")
calculo= calcular_desconto(preco, desconto )
print("o produto com desconto é =", calculo )