try:
    preco=int(input("cloque o valor do produto  :"))
    valor=int(input("coloque o valor do desconto "))
    resultado= (preco *valor )/100
    print(" O preço do produto é : ", preco)
    print(" O valor do desconto é : ", valor)
    print(preco-resultado)
    
except: 

    print(" detectei o caracteri invalido ")
