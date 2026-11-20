import mod_msg
import mod_inputs
import calculadora
def recebe_opçao():
    opçao=mod_inputs.recebe_int("inserir opçao - ")
    match opçao : 
        case 0 : 
            print("sair do programa ")
        case 1 :
           calculadora.calc
        case 2: 
            print(" aqui chamo a calculadora frete!")
        case _: 
            print("opçao invalida \n")
        
def main():
    mod_msg.msg_menu_prinicipal()
