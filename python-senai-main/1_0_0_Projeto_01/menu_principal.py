import mod_msg
import mod_inputs
import calculadora
import cotafrete
def recebe_opçao():
    while True:
        mod_msg.msg_menu_prinicipal()
        opçao=mod_inputs.recebe_int("inserir opçao - ")
        match opçao : 
            case 0 : 
                print("sair do programa ")
            case 1 :
                calculadora.calc()
            case 2: 
                cotafrete.executar()
            case _: 
                print("opçao invalida \n")
def main():
        mod_msg.msg_menu_prinicipal()
        recebe_opçao()

