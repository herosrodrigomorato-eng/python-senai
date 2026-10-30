#estrutura if e else
try:
    idade=int(input("digite sua idade em anos :"))
    if idade > 65 :
        print("você faz parte da terceira idade !")
    else: 
        print("você não é da terceira idade !")

except: 
    print(" digite apenas número !")
