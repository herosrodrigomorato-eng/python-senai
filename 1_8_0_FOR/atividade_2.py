# estrura for 
start=True
while start: 
    try: 
        numero=int(input("digite um numero : "))
        for multiplicador  in  range( 1,11): 
            resultado= numero * multiplicador
            print("numero","x", multiplicador,"=", resultado )
        start=False
    except ValueError:
        print(" coloque um numero valido!")