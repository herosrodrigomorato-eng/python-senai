# estrutura match
try: 
    print(" 1=domingo\n 2=segunda\n 3=terça \n 4=quarta\n 5=quinta \n 6=sexta \n 7=sabado  ")
    dia= int(input("escola um dia da semana :"))
    if (dia >= 1 and dia <=7 ):
        print(" o dia escolhido foi :  ",dia )
        match dia :
            case 1: 
                print ("domingo ")
            case 2: 
                print("segunda")
            case 3: 
                print("terça")
            case 4: 
               print("quarta")
            case 5: 
                print("quinta")
            case 6: 
                print("sexta")
            case 7:
                print("sabado ")
    else: 
         print("numero invalido ")
except:
    print("numero invalido !")

