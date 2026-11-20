import math 
def calc():
    print("===== CALCULADORA =====")
    print("0 - sair()")
    print("1 - Adição (+)")
    print("2 - Subtração (-)")
    print("3 - Multiplicação (*)")
    print("4 - Divisão (/)")
    print("5 - porcentagem (%)")

    while True:
        opcao = input("\nEscolha uma operação: ")

        if opcao == "0":
            print("Calculadora encerrada!")
            break

        if opcao in ["1", "2", "3", "4","5"]:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))

                if opcao == "1":
                    resultado = num1 + num2
                    print("Resultado:", resultado)

                elif opcao == "2":
                    resultado = num1 - num2
                    print("Resultado:", resultado)

                elif opcao == "3":
                    resultado = num1 * num2
                    print("Resultado:", resultado)

                elif opcao == "4":
                    if num2 != 0:
                        resultado = num1 / num2
                        print("Resultado:", resultado)
                else:
                    print("Erro! Não é possível dividir por zero.") 
        elif opcao == "5":
                resultado = num1*(num2/100)
                print("resultado",resultado)

        else:
            print("Opção inválida! Tente novamente.")