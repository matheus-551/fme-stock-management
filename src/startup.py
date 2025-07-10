from services import usuario

usuario_logado = False;

def show_menu_produtos():
    print("===================================");
    print("         Módulo de Produtos        ");
    print("===================================");
    
    print("1. Cadastrar produto sem entrada");
    print("2. Listar produtos");
    print("3. Atualizar dados do produto");
    print("4. Remover produto");
    print("0. Voltar");
    
    opcao = int(input("Selecione a opção desejada: "));
    
    match (opcao):
        case 1:
            print("Cadastrar produto");
        case 2:
            print("Listar produtos");
        case 0:
            show_menu();
        case _:
            print("Opção Inválida. Tente novamente.");
            show_menu_produtos();

def show_menu():
    print("===================================");
    print("         BEM VINDO AO MENU        ");
    print("===================================");
    
    print("1. Entrada de produtos");
    print("2. Produtos");
    print("3. Saida de produtos");
    print("0. Sair");
    
    opcao = int(input("Selecione a opção desejada: "));
    
    match (opcao):
        case 1:
            print("Entrada de produtos");
        case 2:
            show_menu_produtos();
        case 3:
            print("Saida de produtos");
        case 0:
            usuario_logado = False;
            show_menu_login();
        case _:
            print("Opção Inválida. Tente novamente.");
            show_menu();
    
  
def show_menu_login():
    print("1. Entrar");
    print("2. Registrar-se");
    print("0. Sair");
    
    option = int(input("Selecione a opção desejada: "));
    
    match (option):
        case 1:
            if(usuario.login_user()):
                usuario_logado = True;
                show_menu();
        case 2:
            usuario.create_user();
            show_menu_login();
        case 0:
            exit();
        case _:
            print("Opção Inválida. Tente novamente.");
            show_menu_login();
   
   
def show_banner():
    print("===================================");
    print("      FME STOCK CONTROL SYSTEM     ");
    print("===================================");
    
def startup():
    show_banner();
    show_menu_login();
    
if __name__ == "__main__":
    startup()