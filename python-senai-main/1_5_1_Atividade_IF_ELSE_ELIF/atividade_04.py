# estrutura de decisão if, else e elif 
try:
    temperatura=int(input("digite a temperatura em graus celso:"))
    if temperatura <0:
        
        print("congelante")
        
    if temperatura >=0 and temperatura<15:
    
        print("frio")
    if temperatura >=15 and temperatura <=30:
        print("agradavel")
    if temperatura >=30:
        print(" muito quente")
except:
    print("coloque apenas numeros inteiros na temperatura")