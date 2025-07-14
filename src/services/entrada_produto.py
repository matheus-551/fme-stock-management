from lib import fileLibrary
from datetime import datetime

def registrar_entrada_produto():
    while True: 
        codigo_produtos = int(input("digite o codigo do produto: ").strip())
    
        produto = fileLibrary.get_by_id("produtos", codigo_produtos)
        
        if produto == None:
            print("Produto nao encontrado.")
            continue
        
        while True:     
            quantidade = int(input("digite a quantidade: ").strip())
        
            if quantidade <= 0:
                print ("Quantidade invalida.")
                continue
            
            break
        
        break
    
    # Atualiza a quantidade em estoque do produto
    fileLibrary.update("produtos", codigo_produtos, "Quantidade em estoque", quantidade)
    
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
            print(f"{coluna[0]}:{coluna[1]}")
        
        print("")
            
    print("")   
            
    
def atualizar_entrada_produtos():
    print("Qual a entrada deseja atualizar")   
       
    codigo_entrada = int(input("digite o codigo da entrada: "))
          
    entrada = fileLibrary.get_by_id("entrada", codigo_entrada)
    
    codigo_produtos = entrada[1][0][1]
        
    if entrada == None:
        print("Entrada nao encontrada")
        return

    print("Qual informação deseja atualizar ?")
    print("1. Atualizar Código do produto")
    print("2. Atualizar Quantidade")
    print("3. Atualizar Data e hora da entrada")

    opcao = int(input("Digite o numero da opcao desejada: "))

    match (opcao):
        case 1: 
            while True:
                codigo_produtos = int(input("digite o codigo do produto: ").strip())
                
                produto = fileLibrary.get_by_id("produtos", codigo_produtos)
                
                if produto == None:
                    print("Produto nao encontrado.")
                    continue
                
                fileLibrary.update("entrada", codigo_entrada, "Codigo do produto", codigo_produtos)
                
                break
        case 2: 
            while True:
                quantidade = int(input("digite a quantidade: ").strip())
                
                if quantidade <= 0:
                    print ("Quantidade invalida.")
                    continue
                
                fileLibrary.update("produtos", codigo_produtos, "Quantidade em estoque", quantidade)
                
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