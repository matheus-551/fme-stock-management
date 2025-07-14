from lib import fileLibrary

def create_user():
    while True:
        username = input("Digite o nome de usuário: ").strip()
        password = input("Digite a senha: ").strip()
        password_confirm = input("Confirme a senha: ").strip()

        if not username:
            print("Erro: Nome de usuário é obrigatório.")
            return False

        if not password:
            print("Erro: Senha é obrigatória.")
            return False

        if password != password_confirm:
            print("Erro: As senhas não coincidem. Tente novamente.")
            continue

        break
    
    usuario = [
        ["username", username], 
        ["password", password]
    ]
    
    fileLibrary.save("usuarios", usuario)


def login_user() -> bool:
    while True:
        username = input("Digite o nome de usuário: ").strip()
        password = input("Digite a senha: ").strip()

        if username.lower() == "sair":
            print("Encerrando login.")
            return False

        if not username or not password:
            print("Erro: Usuário e senha são obrigatórios.")
            continue

        linhas = fileLibrary.list_all("usuarios")

        for linha in linhas:
            if linha[1][0][1] == username and linha[1][1][1] == password:
                print("Login realizado com sucesso!")
                return True

        print("Usuário ou senha inválidos. Tente novamente.")