from lib import fileLibrary
from datetime import datetime

def registrar_entrada_produto():
    while True: 
        codigo_produtos = input("digite o codigo do produto: ").strip()
        
        if not codigo_produtos.isnumeric():
            print("Erro: Codigo do produto deve ser um número.")
            continue
        
        codigo_produtos = int(codigo_produtos)
    
        produto = fileLibrary.get_by_id("produtos", codigo_produtos)
        
        if produto == None:
            print("Produto nao encontrado.")
            continue
        
        while True:     
            quantidade = input("digite a quantidade: ").strip()
            
            if not quantidade.isnumeric():
                print("Erro: Quantidade deve ser um número.")
                continue
        
            quantidade = int(quantidade)
        
            if quantidade <= 0:
                print ("Quantidade invalida.")
                continue
            
            break
        
        break
    
    # Atualiza a quantidade em estoque do produto
    fileLibrary.update("produtos", codigo_produtos, "Quantidade em estoque", (quantidade + produto[1][3][1]))
    
    entrada_produtos = [
        ["Codigo do produto", codigo_produtos],
        ["Quantidade", quantidade],
        ["data e hora da entrada", datetime.now().strftime("%d/%m/%Y %H:%M:%S")]
    ]
    
    # Registra uma entrada de produtos
    fileLibrary.save("entrada", entrada_produtos)
    
def listar_entrada():
    print("")
    
    entradas = fileLibrary.list_all("entrada")
    if len (entradas) == 0:
        print("nenhuma entrada cadastrada.")
        return
    
    for entrada in entradas:
        print(f"Codigo da entrada: {entrada[0]}")
        
        for coluna in entrada[1]:
            print(f"{coluna[0]}: {coluna[1]}")
        
        print("")
            
    print("")   
            
    
def atualizar_entrada_produtos():
    print("Qual a entrada deseja atualizar")   
       
    codigo_entrada = input("digite o codigo da entrada: ")
    
    if not codigo_entrada.isnumeric():
        print("Erro: Codigo da entrada deve ser um número.")
        atualizar_entrada_produtos()
        
    codigo_entrada = int(codigo_entrada)
          
    entrada = fileLibrary.get_by_id("entrada", codigo_entrada)
    
    codigo_produtos = entrada[1][0][1]
    
    produto = fileLibrary.get_by_id("produtos", codigo_produtos)
                
    if produto == None:
        print("Produto nao encontrado.")
        return

    if entrada == None:
        print("Entrada nao encontrada")
        return

    print("Qual informação deseja atualizar ?")
    print("1. Atualizar Código do produto")
    print("2. Atualizar Quantidade")
    print("3. Atualizar Data e hora da entrada")

    opcao = input("Digite o numero da opcao desejada: ")
    
    if not opcao.isnumeric():
        print("Opção Inválida. Tente novamente.")
        atualizar_entrada_produtos()
        
    opcao = int(opcao)

    match (opcao):
        case 1: 
            while True:
                codigo_produtos = input("digite o codigo do produto: ").strip()
                
                if not codigo_produtos.isnumeric():
                    print("Erro: Codigo do produto deve ser um número.")
                    continue
                
                codigo_produtos = int(codigo_produtos)
                
                produto = fileLibrary.get_by_id("produtos", codigo_produtos)
                
                if produto == None:
                    print("Produto nao encontrado.")
                    continue
                
                fileLibrary.update("entrada", codigo_entrada, "Codigo do produto", codigo_produtos)
                
                break
        case 2: 
            while True:
                quantidade = input("digite a quantidade: ").strip()
                
                if not quantidade.isnumeric():
                    print("Erro: Quantidade deve ser um número.")
                    continue
                
                quantidade = int(quantidade)
                
                if quantidade <= 0:
                    print ("Quantidade invalida.")
                    continue
                
                quantidade_calculada = calcula_quantidade_estoque(quantidade, entrada[1][1][1], produto[1][3][1])
                
                fileLibrary.update("produtos", codigo_produtos, "Quantidade em estoque", quantidade_calculada)
                
                fileLibrary.update("entrada", codigo_entrada, "Quantidade", quantidade)
                
                break
        case 3: 
            while True:
                data_hora = input("digite a nova data e hora (dd/mm/aaaa hh:mm:ss): ")
                
                if data_hora == "":
                    print("Data e hora invalida. Tente novamente.")
                    continue
                
                fileLibrary.update("entrada", codigo_entrada, "data e hora da entrada", data_hora)
                
                break
        case _:
            print("Opção Inválida. Tente novamente.")
            atualizar_entrada_produtos()
            
            
def calcula_quantidade_estoque(nova_quantidade, quantidade_entrada, quantidade_estoque):
    if nova_quantidade > quantidade_entrada:
        return quantidade_estoque + (nova_quantidade - quantidade_entrada)
    else:
        return quantidade_estoque - (quantidade_entrada - nova_quantidade)