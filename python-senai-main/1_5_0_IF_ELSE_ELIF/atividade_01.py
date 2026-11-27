#estrutura if elif e else
try:
    idade=int(input("coloque sua idade :"))
    if idade < 0:
         print("idade invalida !")

    if idade <12:
            print("você é uma criança !")
    if idade > 12 :
        if idade  <= 17 :
                print("você é adolecente !")
    if idade >=18 :
            print("você ja é um adulto !")
except:
    print("coloque apenas numeros !")
    