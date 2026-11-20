import mod_msg
import mod_inputs
import menu_principal 
USUARIO="heros"
SENHA="30041"
def valida_usuario(user):
    while True:
        usuario= mod_inputs.recebe_str("digite seu usuario : ")
        if len(usuario) >= 5:
            if user == usuario:
                break
            else: 
                print("usuario incorreto !\n")
        else: 
            print("a senha deve conter 5 caracteres")
    return usuario 
def valida_senha(senha1): 
    while True:
        senha=mod_inputs.recebe_senha("digite sua senha : ")
        if senha == senha1:
            break
        else: 
            print("senha invalida! \n")
    return senha 

def main():
    mod_msg.msg_login_ini()
    usuario_validado = valida_usuario(USUARIO)
    senha_valida=valida_senha(SENHA)
    mod_msg.msg_minu_principal()
   
