#estrutura if else 
try:
    nota=float(input("coloque a nota : "))
    if nota <0 or nota >10: 
        print("nota invalida !")
    elif nota >=0 and nota <4.9:
        print("nota reprovada !")
    elif nota >=5 and nota <=6.9: 
        print("ficou de recuperação ")
    else:
        print("aprovado !")
except:
    print("digite uma nota valida !")
