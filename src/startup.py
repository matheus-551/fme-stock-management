from services import usuario
from services import produto
from services import entrada_produto
from services import saida_produtos

usuario_logado = False;

def show_menu_saida_produtos():
    print("===================================");
    print("         Módulo de Saída          ");
    print("===================================");
    
    print("1. Saída de produtos")
    print("2. Listar saidas de produtos")
    print("3. Atualizar saida de produtos")
    print("0. Voltar");
    
    opcao = input("Selecionar a opcao desejada :").strip()
    
    if not opcao.isnumeric():
        print("Opção Inválida. Tente novamente.")
        show_menu_saida_produtos()
    
    opcao = int(opcao)
        
    match(opcao):
        case 1: 
            print("Saida de produtos")
            saida_produtos.registrar_saida_produtos()
            show_menu_saida_produtos()
        case 2: 
            print("Listar saidas de produtos")
            saida_produtos.listar_saida_produtos()
            show_menu_saida_produtos()
        case 3:
            print("Atualizar saida de produtos")
            saida_produtos.atualizar_saida_produtos()
            show_menu_saida_produtos()
        case 0: 
            show_menu()    
        case _:
            print("Opção Inválida. Tente novamente.");    
            show_menu_saida_produtos()

def show_menu_entrada_produtos():
    print("===================================");
    print("         Módulo de Entrada        ");
    print("===================================");
    
    print("1. Entrada de produtos")
    print("2. Listar entrada de produtos")
    print("3. Atualizar entrada de produtos")
    print("0. Voltar");
    
    opcao = input("Selecionar a opcao desejada :").strip()
    
    if not opcao.isnumeric():
        print("Opção Inválida. Tente novamente.")
        show_menu_entrada_produtos()
    
    opcao = int(opcao)
    
    match(opcao):
        case 1: 
            print("Entrada de produtos")
            entrada_produto.registrar_entrada_produto()
            show_menu_entrada_produtos()
        case 2: 
            print("Listar Entrada de produtos")
            entrada_produto.listar_entrada()
            show_menu_entrada_produtos()
        case 3: 
            print("Atualizar entrada de produtos")
            entrada_produto.atualizar_entrada_produtos()
            show_menu_entrada_produtos()
        case 0: 
            show_menu()    
        case _:
            print("Opção Inválida. Tente novamente.");    
            show_menu_entrada_produtos()
    
    
def show_menu_produtos():
    print("===================================");
    print("         Módulo de Produtos        ");
    print("===================================");
    
    print("1. Cadastrar produto sem entrada");
    print("2. Listar produtos");
    print("3. Atualizar dados do produto");
    print("4. Remover produto");
    print("0. Voltar");
    
    opcao = input("Selecionar a opcao desejada :").strip()
    
    if not opcao.isnumeric():
        print("Opção Inválida. Tente novamente.")
        show_menu_produtos()
    
    opcao = int(opcao)
    
    match (opcao):
        case 1:
            print("Cadastrar produto");
            produto.criar_produto_sem_entrada();
            show_menu_produtos()
        case 2:
            print("Listar produtos");
            produto.listar_produtos();
            show_menu_produtos()
        case 3:
            print("Atualizar dados do produto");
            produto.atualizar_dados_produto();
            show_menu_produtos()
        case 4:
            print("Remover produto");
            produto.remover_produto();
            show_menu_produtos()
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
    
    opcao = input("Selecionar a opcao desejada :").strip()
    
    if not opcao.isnumeric():
        print("Opção Inválida. Tente novamente.")
        show_menu()
    
    opcao = int(opcao)
    
    match (opcao):
        case 1:
            show_menu_entrada_produtos();
        case 2:
            show_menu_produtos();
        case 3:
            show_menu_saida_produtos();
        case 0:
            usuario_logado = False;
            show_menu_login();
        case _:
            print("Opção Inválida. Tente novamente.");
            show_menu();
    
  
def show_menu_login():
    print("1. Entrar");
    print("2. Registrar-se");
    print("0. Finalizar");
    
    opcao = input("Selecionar a opcao desejada :").strip()
    
    if not opcao.isnumeric():
        print("Opção Inválida. Tente novamente.")
        show_menu_login()
    
    opcao = int(opcao)
    
    match (opcao):
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
    
# Função responsável por iniciar a aplicação
def startup():
    show_banner();
    show_menu_login();
    
if __name__ == "__main__":
    startup()