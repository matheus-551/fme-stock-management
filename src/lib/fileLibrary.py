import os

### @Author: Matheus Falcão
 
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "storage"))
 
def save(nome_arquivo, dados) -> None:
    """
    Registra um novo conjunto de dados no arquivo.
    Se o arquivo não existir, ele será criado.
    Cada linha será registrada no formato: [identificador, [["Chave", "Valor"], ...]
    
    Args:
        nome_arquivo (str): Nome do arquivo.
        dados (list): Dados a serem registrados.
    
    """
    caminho = os.path.join(BASE_DIR, nome_arquivo + ".txt")
    identificador = 1

    if os.path.exists(caminho):
        with open(caminho, "r") as arquivo:
            linhas = arquivo.readlines()
            if linhas:
                ultimos_ids = [eval(linha.strip())[0] for linha in linhas]
                identificador = max(ultimos_ids) + 1

    linha = str([identificador, dados]) + "\n"
    with open(caminho, "a") as arquivo:
        arquivo.write(linha)

    print("Registro salvo com sucesso.")

def list_all(nome_arquivo) -> list:
    """
    Leitura de dados armazenados em um arquivo.
    
    Args:
        nome_arquivo (str): Nome do arquivo.
    
    Returns: 
        list: Dados lidos do arquivo
    """
    caminho = os.path.join(BASE_DIR, nome_arquivo + ".txt")
    if not os.path.exists(caminho):
        return []

    with open(caminho, "r") as arquivo:
        linhas = arquivo.readlines()

    registros = []
    for linha in linhas:
        registros.append(eval(linha.strip()))

    return registros

def get_by_id(nome_arquivo, identificador) -> str:
    """
    Busca um conjunto de dados pelo identificador.
    
    Args:
        nome_arquivo (str): Nome do arquivo.
        identificador (str): Identificador do conjunto de dados.
    
    Returns: 
        str: Dados lidos do arquivo
    """
    linhas = list_all(nome_arquivo)
    
    for linha in linhas:
        if linha[0] == int(identificador):
            return linha
    
    return None
    

def update(nome_arquivo, identificador, chave, novo_valor) -> None:
    """
    Atualiza um conjunto de dados pelo identificador.
    
    Args:
        nome_arquivo (str): Nome do arquivo.
        identificador (str): Identificador do conjunto de dados.
        chave (str): Chave do par a ser atualizado.
        novo_valor (str): Novo valor do par.
    """
    caminho = os.path.join(BASE_DIR, nome_arquivo + ".txt")
    linhas = list_all(nome_arquivo)
    nova_lista = []

    for linha in linhas:
        if linha[0] == int(identificador):
            for par in linha[1]:
                if par[0] == chave:
                    par[1] = novo_valor
            nova_lista.append(str(linha) + "\n")
        else:
            nova_lista.append(str(linha) + "\n")

    with open(caminho, "w") as arquivo:
        arquivo.writelines(nova_lista)

    print("Registro atualizado com sucesso.")
    print("")
    
def remove(nome_arquivo, identificador):
    caminho = os.path.join(BASE_DIR, nome_arquivo + ".txt")

    registro = get_by_id(nome_arquivo, identificador)
    
    if not registro:
        print("Registro nao encontrado.")
        return
    
    registro = None
    linhas = list_all(nome_arquivo)
    nova_lista = []

    for linha in linhas:
        try:
            if linha[0] != int(identificador):
                nova_lista.append(str(linha) + "\n")
        except:
            nova_lista.append(str(linha) + "\n")

    with open(caminho, "w") as arquivo:
        arquivo.writelines(nova_lista)

    print("Registro removido com sucesso.")
    print("")