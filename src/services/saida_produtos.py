from lib import fileLibrary
from datetime import datetime

def registrar_saida_produtos():
    print("Registrar saida de produtos")
    
    quantidade_calculada = None
    
    while True:
        codigo_produtos = int(input("digite o codigo do produto: ").strip())
    
        produto = fileLibrary.get_by_id("produtos", codigo_produtos)
        
        if produto == None:
            print("Produto nao encontrado.")
            continue
        
        quantidade_calculada = produto[1][3][1]
        
        while True:     
            quantidade = int(input("digite a quantidade: ").strip())
        
            if quantidade <= 0:
                print ("Quantidade invalida.")
                continue
            
            if quantidade > quantidade_calculada:
                print("Quantidade maior que a quantidade em estoque.")
                continue
            
            break
        
        break
    
    quantidade_calculada = quantidade_calculada - quantidade
    
    saida_produtos = [
        ["Codigo do produto", codigo_produtos],
        ["Quantidade", quantidade],
        ["Valor total", calcula_valor_total(quantidade, produto[1][1][1])],
        ["data e hora da saida", datetime.now().strftime("%d/%m/%Y %H:%M:%S")]
    ]
    
    # Atualiza a quantidade em estoque do produto
    fileLibrary.update("produtos", codigo_produtos, "Quantidade em estoque", quantidade_calculada)
    
    fileLibrary.save("saida", saida_produtos)
          
def listar_saida_produtos():
    print("")
    
    saidas = fileLibrary.list_all("saida")
    
    if len (saidas) == 0:
        print("nenhuma saida cadastrada.")
        return
    
    for saida in saidas:
        print(f"Codigo da saida: {saida[0]}")
        
        for coluna in saida[1]:
            print(f"{coluna[0]}: {coluna[1]}")
        
        print("")
            
    print("")
    
def atualizar_saida_produtos():
    print("Qual saida deseja atualizar?")
    
    codigo_saida = int(input("Digite o codigo da saida: "))
    
    saida = fileLibrary.get_by_id("saida", codigo_saida)
    
    if saida == None:
        print("saida nao encontrada.")
        return
    
    print("Qual informação deseja atualizar ?")
    print("1. Atualizar Código do produto")
    print("2. Atualizar Quantidade")
    print("3. Atualizar Data e hora da saida")
    
    opcao = int(input("Digite o numero da opcao desejada: "))
    
    match (opcao):
        case 1: 
            while True:
                codigo_produtos = int(input("digite o codigo do produto: ").strip())
                
                produto = fileLibrary.get_by_id("produtos", codigo_produtos)
                
                if produto == None:
                    print("Produto nao encontrado.")
                    continue
                
                fileLibrary.update("saida", codigo_produtos, "Codigo do produto", codigo_produtos)
                
                break
        case 2:
            while True:
                quantidade = int(input("digite a quantidade: ").strip())
                produto = fileLibrary.get_by_id("produtos", saida[1][0][1])
        
                if quantidade <= 0:
                    print ("Quantidade invalida.")
                    continue
                
                
                
                quantidade_calculada = calcula_quantidade(quantidade, saida[1][1][1], produto[1][3][1])
                valor_total = calcula_valor_total(quantidade_calculada, produto[1][1][1])
                
                fileLibrary.update("saida", codigo_saida, "Quantidade", quantidade)
                fileLibrary.update("saida", codigo_saida, "Valor total", valor_total)
                fileLibrary.update("produtos", saida[1][0][1], "Quantidade em estoque", calcula_quantidade(quantidade, saida[1][1][1], produto[1][3][1]))
                
                break
        case 3: 
            while True:
                data_hora = input("digite a nova data e hora (dd/mm/aaaa hh:mm:ss): ")
                
                if data_hora == "":
                    print("Data e hora invalida. Tente novamente.")
                    continue
                
                fileLibrary.update("saida", codigo_saida, "data e hora da saida", data_hora)
                
                break
        case _:
            print("Opção Inválida. Tente novamente.")
            atualizar_saida_produtos()

        
def calcula_quantidade(nova_quantidade_saida, quantidade_saida, quantidade_produto):
    if nova_quantidade_saida > quantidade_saida:
        quantidade_calculada = quantidade_produto + (nova_quantidade_saida - quantidade_saida)
    else:
        quantidade_calculada = quantidade_produto - (quantidade_saida - nova_quantidade_saida)
    
    return quantidade_calculada

def calcula_valor_total(quantidade, valor_unitario):
    return int(quantidade) * float(valor_unitario)