def loginUsuario(perfil):
    if perfil == 'admin':
        print("Bem-vindo, Administrador.")
    else:
        print("Bem-vindo, Usuário")
entrada = str(input("Digite o usuário: ").lower())
loginUsuario(entrada)