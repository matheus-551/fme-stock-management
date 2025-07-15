from lib import fileLibrary

def criar_produto_sem_entrada():
    while True:
        nome_produto = input("Digite o nome do produto: ").strip()
        valor_unitario = input("Digite o valor unitário: ").strip()
        tipo_produto = input("Digite o tipo do produto: ").strip()
        eh_produto_perecivel = input("O produto é perecível? Digite (S/N): ").strip().upper()
        data_validade = None
        
        if eh_produto_perecivel != "S" and eh_produto_perecivel != "N":
            print("Opção inválida. Tente novamente.")
            eh_produto_perecivel = input("O produto é perecível? Digite (S/N): ").strip().upper()
            
        if eh_produto_perecivel == "N":
            eh_produto_perecivel = False
        else:
            eh_produto_perecivel = True
            data_validade = input("Digite a data de validade: ").strip()

        if not nome_produto or not valor_unitario or not tipo_produto:
            print("Erro: Todos os campos devem ser preenchidos.")
            continue
        
        if not valor_unitario.isnumeric():
            print("Erro: Valor unitario deve ser um número.")
            continue
        
        break
    
    valor_unitario = valor_unitario.replace(",", ".")
    
    produto = [
        ["Nome do produto", nome_produto], 
        ["Valor unitário", float(valor_unitario)], 
        ["Tipo do produto", tipo_produto], 
        ["Quantidade em estoque", 0],
        ["É perecível ?", eh_produto_perecivel], 
        ["Data de validade", data_validade]   
    ]
    
    fileLibrary.save("produtos", produto)    
    
def listar_produtos():
    print()
    
    produtos = fileLibrary.list_all("produtos")
    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
        return

    for produto in produtos:
        print(f"Código Produto: {produto[0]}")
        for coluna in produto[1]:          
            print(f"{coluna[0]}: {coluna[1]}")
        print("")
        
    print("")
        

def atualizar_dados_produto():
    print("Qual produto deseja atualizar?")
    
    codigo_produto = input("Digite o codigo do produto: ")
    
    if not codigo_produto.isnumeric():
        print("Erro: Codigo do produto deve ser um número.")
        atualizar_dados_produto()
        
    codigo_produto = int(codigo_produto)
    
    produto = fileLibrary.get_by_id("produtos", codigo_produto)
    
    if produto == None:
        print("Produto nao encontrado.")
        return
    
    print("Qual informação deseja atualizar ?")
    print("1. Atualizar nome do produto")
    print("2. Atualizar valor unitario")
    print("3. Atualizar tipo do produto")
    print("4. Atualizar se o produto é perecivel")
    print("5. Atualizar data de validade")
    
    opcao = input("Digite o numero da opcao desejada: ")
    
    if not opcao.isnumeric():
        print("Erro: Opção deve ser um número.")
        atualizar_dados_produto()
        
    opcao = int(opcao)
    
    match (opcao):
        case 1:
            while True:
                nome_produto = input("Digite o novo nome do produto: ").strip()

                if not nome_produto:
                    print("Erro: Nome do produto é obrigatório.")
                    continue

                fileLibrary.update("produtos", codigo_produto, "Nome do produto", nome_produto)
                
                break
        case 2:
            while True:
                valor_unitario = input("Digite o novo valor unitario: ").strip()
                valor_unitario = valor_unitario.replace(",", ".")

                if not valor_unitario:
                    print("Erro: Valor unitario é obrigatório.")
                    continue
                
                if not valor_unitario.isnumeric():
                    print("Erro: Valor unitario deve ser um número.")
                    continue

                fileLibrary.update("produtos", codigo_produto, "Valor unitário", float(valor_unitario))
                
                break
        case 3:
            while True:
                tipo_produto = input("Digite o novo tipo do produto: ").strip()

                if not tipo_produto:
                    print("Erro: Tipo do produto é obrigatório.")
                    continue

                fileLibrary.update("produtos", codigo_produto, "Tipo do produto", tipo_produto)
                
                break
        case 4:
            while True:
                eh_produto_perecivel = input("O produto é perecível? Digite (S/N): ").strip().upper()
                
                if eh_produto_perecivel != "S" and eh_produto_perecivel != "N":
                    print("Opção inválida. Tente novamente.")
                    eh_produto_perecivel = input("O produto é perecível? Digite (S/N): ").strip().upper()
                    
                if eh_produto_perecivel == "N":
                    eh_produto_perecivel = False
                else:
                    eh_produto_perecivel = True

                fileLibrary.update("produtos", codigo_produto, "É perecível ?", eh_produto_perecivel)
                
                break
        case 5:
            while True:
                data_validade = input("Digite a nova data de validade: ").strip()

                if not data_validade:
                    print("Erro: Data de validade é obrigatória.")
                    continue

                fileLibrary.update("produtos", codigo_produto, "Data de validade", data_validade)
                
                break
        case _:
            print("Opção Inválida. Tente novamente.")
            atualizar_dados_produto();
    
def remover_produto():
    print("Qual produto deseja remover?")
    
    codigo_produto = input("Digite o codigo do produto: ")
    
    if not codigo_produto.isnumeric():
        print("Erro: Codigo do produto deve ser um número.")
        remover_produto()
        
    codigo_produto = int(codigo_produto)
    
    produto = fileLibrary.get_by_id("produtos", codigo_produto)
    
    if produto == None:
        print("Produto nao encontrado.")
        return
    
    fileLibrary.remove("produtos", codigo_produto)