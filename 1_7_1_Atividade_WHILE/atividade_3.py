# estrutura while

while True:  
    try:
        numero =int(input("coloque um numero: "))
        break
    except:
        print(" foi detectado uma letra, num campo que é exclusivo para numero!")
contador=1 
while contador !=11: 
    resultado = contador * numero 
    print(contador,"x",numero,"=", resultado)
    contador += 1
     
    
